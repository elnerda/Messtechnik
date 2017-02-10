import platform
import serial

xx=platform.system()
print xx
if xx.startswith('Win'):
	print "das ist windows"
	var=input("Please enter your Serialport number ")
	#var2='COM'+str(var)
	ser = serial.Serial(var2,9600,timeout=1)
	time.sleep(3)


	
	while 1:
		ser.write("c")
		x=ser.read(5)
		print "Temperatur in Celsius betraegt: " +x
		time.sleep(0.75)
		ser.write("f")
		y=ser.read(5)
		print "Temperatur in Fahrenheit betraegt: "+y
		time.sleep(0.75)
	
elif xx.startswith('Lin'):
	print "das ist linux"
	a=serial_ports()

	ser = serial.Serial(a[1],9600,timeout=1)	#eventuell mit if und -1 der abfrage des arrays
	time.sleep(3)


	
	while 1:
		ser.write("c")
		x=ser.read(5)
		print "Temperatur in Celsius betraegt: " +x
		time.sleep(0.75)
			