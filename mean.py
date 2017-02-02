#Script zur berechnung von Mittelwert, Varianz und Standardabweichung von Messwerten
#Gaetano Fresa 28.11.2016 5:22 PM GMT+1


import math
print "Please declare # of samples: "
anzahl=input()
print "Please declare sample unit: "
einheit=raw_input()
werte=[]
print "Please input samples, after ech sample hit return:"


for a in range (0,anzahl):
	werte.append(input())
print werte
mw=0
#mittelwert wird berechnet

val=0
for b in range (len(werte)):
	val=val+werte[b]

print "arithmetic mean: "
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
print "standard variance: "
print s, einheit
print " "
