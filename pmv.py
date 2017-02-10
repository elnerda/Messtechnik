# PMV-Berechnung U-CUBE 2016
# Version 08 31.12.2016
# by Yoyo Dlabal

# Import von Modulen
import math, decimal

from decimal import Decimal as D         # Abkuerzung fuer Dezimalzahl

# Definitionen

clo=D(0.5)
met=D(1.6)
w=D(0.0)

# Messwerte

ta=D(27.0)              # Lufttemperatur
tr=D(27.0)              # Strahlungstemperatur
vel=D(0.3)              # Luftgeschwindigkeit
rh=D(60.0)              # Relative Luftfeuchtigkeit

# abgeleitete Konstanten

taa=D(ta+D(273.0))         # Lufttemperatur in K
tra=D(tr+D(273.0))         # Strahlungstemperatur in K
pa=rh*D(10.0)*D((D(16.6536)-(D(4030.183) / (ta+D(235.0))))).exp()   # Partialdruck Wasserdampf
icl=D(0.155)*clo            # Kleidungsisolationswert
m=D(58.15)*met             # Energieumsatz
mw=m-w                      # Waermeleistung des Koerpers
fcl1=D(1.0)+D(1.29)*icl     #
fcl2=D(1.05)+D(0.645)*icl   # 0.645 oder 1.645 Widerspruch in 7730 wirkt sich bei clo=1 nicht aus
if (icl>0.078): fcl=fcl1    #
else:                       #
    fcl=fcl2                # Kleidungsflaechenfaktor

# Iteration der Oberflaechentemperatur der Kleidung

tcla=taa+(D(35.5)-ta)/(D(3.5)*(D(6.45)*(icl+D(0.1))))   # erste Abschaetzung
x1=tcla/100     # Rechengroesse1 (tcla/100)
x2=x1           # Rechengroesse2 (tcla/100)

hcn=D(2.38)*(abs(D(100)*x2-taa))**(D(0.25)) # waermeuebergangskoeffizient fuer natuerliche Konvektion in W/qmK
hcf=D(12.1)*D(vel).sqrt() # Waermeuebergangskoeffizient fuer erzwungene Konvektion in W/qmK
if (hcf>hcn):
    hc=hcf
else:
    hc=hcn #Waermeuebergangskoeffizient

x1=(D(273+35.7)-D(.028)*mw-icl*fcl*D(3.96)*(x2**D(4)-(tra/D(100))**D(4))-icl*fcl*hc*((D(100)*x2)-taa))/D(100) # zweite Abschaetzung

# Iterationsschleife

n=0 # Zaehler fuer Iterationen
eps=0.0001 # Abbruchbedingung fuer Rechengroessen x1 und x2

while(n<100):
    while(abs(x1-x2)>eps):
        x1=D((x1+x2)/2) # Mittelwertbildung der Rechengroessen
        hcn=D(2.38)*(abs(D(100)*x1-taa))**(D(0.25)) # neuer natuerlicher Waermeuebergangskoeffizient
        if (hcf>hcn): hc=hcf
        else: hc=hcn
        x4=D(x1**4)
        t4=D((tra/D(100))**4)
        dtR=D(x4-t4)
        rad=D(icl*fcl*D(3.96)*dtR) # Strahlungsanteil der Waermeabgabe
        dtC=D(100)*x1-taa
        con=D(icl*fcl*hc*dtC) # Konvektionsanteil der Waermeabgabe
        x2=(D(273)+D(35.7)-D(0.028)*mw-rad-con)/D(100) # verbesserte Rechengroesse
    n=n+1

tcl=D(100)*x2-D(273)  # Kleidungsoberflaechentemperatur in Celsius
tcla=D(100)*x2     # Kleidungsoberflaechentemperatur in Kelvin
print "tcl = ", tcl

# Berechnung des waermeverlustes

hl1=D(3.05)*D(0.001)*(D(5733)-D(6.99)*mw-pa) # waermeverlust durch die haut
if(mw>58.15): hl2=D(0.42)*(mw-D(58.15)) # waermeverlust durch Schwitzen
else: hl2=0
hl3=D(1.7)*D(0.00001)*m*(D(5867)-pa) # waermeverlust durch feuchtes ausatmen
hl4=D(0.0014)*m*(D(34)-ta) # waermeverlust durch trockenes ausatmen
hl5=D(3.96)*fcl*(((tcla/D(100))**4)-(tra/D(100))**4) # waermeverlust durch Strahlung
hl6=fcl*hc*(tcl-ta) # waermeverlust durch Konvektion

# Berechnung von PMV und PPD

ts=D(0.303)*D(D(-0.036)*m).exp()+D(0.028) # uebergangskoeffizient fuer das waermegefuhl nach FANGER
pmv=ts*(mw-hl1-hl2-hl3-hl4-hl5-hl6) # pmv nach DIN 7730
ppd=D(100.0)-D(95.0)*D(((D(-0.03353)*pmv**4)-D(0.2178)*pmv**2)).exp() # ppd nach DIN 7730
print "pmv = ", pmv, "ppd = ", ppd

