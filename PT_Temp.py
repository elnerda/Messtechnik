#!/bin/python

import math
a=0.00385

while True:
	print "Bitte PT-Nennwiderstand eingeben"
	R0=input()
	print "Bitte gemessenen Widerstand eingeben"
	Rpt=input()
	#---Temperatur berechnen----
	dt=(((Rpt/R0)-1)/a)
	print "Die Temperatur betraegt: " + str(dt)
	print""
	
