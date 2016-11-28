#Script zur berechnung von Mittelwert, Varianz und Standardabweichung von Messwerten
#Gaetano Fresa 28.11.2016 17:22


import math
print "Bitte Anzahl der Messwerte eingeben: "
anzahl=input()
print "Bitte Einheit der Messwerte eingeben: "
einheit=raw_input()
werte=[]
print "Bitte Messwerte eingeben"


for a in range (0,anzahl):
	werte.append(input())
print werte
mw=0
#mittelwert wird berechnet

val=0
for b in range (len(werte)):
	val=val+werte[b]

print "Der Mittelwert betraegt: "
mw=val/len(werte)
print mw ,einheit
print " "
#Varianz berechnen
delta=[]
for c in range (len(werte)):
	delta.append(math.pow(werte[c]-mw,2))
	

val1=0
for b in range (len(delta)):
	val1=val1+delta[b]
dt=val1/(len(werte)-1)
print dt, einheit
print " "

s=math.sqrt(dt)
print "Die Standardabweichung der Einzelmesswerte betraegt: "
print s, einheit
print " "