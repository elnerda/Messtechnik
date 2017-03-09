import serial
import time
import sys
import glob
import platform

from datetime import datetime
from timeit import default_timer as timer
wait=0.1
def serial_ports():
    
    if sys.platform.startswith('win'):
        ports = ['COM' + str(i + 1) for i in range(256)]

    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this is to exclude your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')

    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


result = serial_ports()
xx=platform.system()
print xx
fo=open("temps.txt","a+")
fo.write("Datum,E51,E55,S51,S55,W51,W55,N51,N55,B51,B55,D51,D55")
fo.write("\n")
fo.close()


if not result:
	print "No Serialport available"
	print "Press STRG+C to close"
else:
	print "Available Serialports"
	print serial_ports()
	print
	if xx.startswith('Win'):
		var=input("Please select your Serialport :COM")
		var2='COM'+str(var)
		print("Connected to ")+var2
		ser = serial.Serial(var2,9600,timeout=1)
		print("Fetching data takes 10 seconds!")
		time.sleep(10)


	
		while 1:
			start=timer()
			ser.write("1")
			t1=ser.read(10)
			print "Temperatur1 in C: " +t1
			time.sleep(wait)		#zeit zum warten
			ser.write("2")
			t2=ser.read(10)
			print "Temperatur2 in C: " +t2
			time.sleep(wait)		#zeit zum warten
			ser.write("3")
			t3=ser.read(10)
			print "Temperatur3 in C: " +t3
			time.sleep(wait)
			ser.write("4")
			t4=ser.read(10)
			print "Temperatur4 in C: " +t4
			time.sleep(wait)		#zeit zm warten
			ser.write("5")
			t5=ser.read(10)
			print "Temperatur5 in C: " +t5
			time.sleep(wait)		#zeit zm warten
			ser.write("6")
			t6=ser.read(10)
			print "Temperatur6 in C: " +t6
			time.sleep(wait)		#zeit zm warten
			ser.write("7")
			t7=ser.read(10)
			print "Temperatur7 in C: " +t7
			time.sleep(wait)		#zeit zm warten
			ser.write("8")
			t8=ser.read(10)
			print "Temperatur8 in C: " +t8
			time.sleep(wait)		#zeit zm warten
			ser.write("9")
			t9=ser.read(10)
			print "Temperatur9 in C: " +t9
			time.sleep(wait)		#zeit zm warten
			ser.write("a")
			t10=ser.read(10)
			print "Temperatur10 in C: " +t10
			time.sleep(wait)		#zeit zm warten
			ser.write("b")
			t11=ser.read(10)
			print "Temperatur11 in C: " +t11
			time.sleep(wait)		#zeit zm warten
			ser.write("c")
			t12=ser.read(10)
			print "Temperatur12 in C: " +t12
			time.sleep(wait)		#zeit zm warten


			###IN DATEI temps.txt SCHREIBEN#####
			time.sleep(wait)
			str1=str(t1)
			str2=str(t2)
			str3=str(t3)
			str4=str(t4)
			str5=str(t5)
			str6=str(t6)
			str7=str(t7)
			str8=str(t8)
			str9=str(t9)
			str10=str(t10)
			str11=str(t11)
			str12=str(t12)
			localtime=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			print(localtime)
			newstr= ",".join((localtime,str1,str2,str3,str4,str5,str6,str7,str8,str9,str10,str11,str12))

			print newstr
			print "In Datei temps.txt speichern"
			fo=open("temps.txt","a+")
			fo.write(newstr)
			fo.write("\n")
			fo.write("\r")
			fo.close()
			end=timer()
			elapsedtime=end-start
			print("time elapsed: ")+str(elapsedtime)
			time.sleep(60-elapsedtime)
			

			
	
	elif xx.startswith('Lin'):
		print "Zu testzwecken fixen Seriellen Port oeffnen"
		time.sleep(0.5)
		a=serial_ports()
		print "automatically connecting to Serialport "+a[0]
		ser = serial.Serial(a[0],9600,timeout=1)	#eventuell mit if und -1 der abfrage des arrays
		time.sleep(3)


	
		while 1:
			start=timer()
			ser.write("1")
			t1=ser.read(10)
			print "Temperatur1 in C: " +t1
			time.sleep(wait)		#zeit zum warten
			ser.write("2")
			t2=ser.read(10)
			print "Temperatur2 in C: " +t2
			time.sleep(wait)		#zeit zum warten
			ser.write("3")
			t3=ser.read(10)
			print "Temperatur3 in C: " +t3
			time.sleep(wait)
			ser.write("4")
			t4=ser.read(10)
			print "Temperatur4 in C: " +t4
			time.sleep(wait)		#zeit zm warten
			ser.write("5")
			t5=ser.read(10)
			print "Temperatur5 in C: " +t5
			time.sleep(wait)		#zeit zm warten
			ser.write("6")
			t6=ser.read(10)
			print "Temperatur6 in C: " +t6
			time.sleep(wait)		#zeit zm warten
			ser.write("7")
			t7=ser.read(10)
			print "Temperatur7 in C: " +t7
			time.sleep(wait)		#zeit zm warten
			ser.write("8")
			t8=ser.read(10)
			print "Temperatur8 in C: " +t8
			time.sleep(wait)		#zeit zm warten
			ser.write("9")
			t9=ser.read(10)
			print "Temperatur9 in C: " +t9
			time.sleep(wait)		#zeit zm warten
			ser.write("a")
			t10=ser.read(10)
			print "Temperatur10 in C: " +t10
			time.sleep(wait)		#zeit zm warten
			ser.write("b")
			t11=ser.read(10)
			print "Temperatur11 in C: " +t11
			time.sleep(wait)		#zeit zm warten
			ser.write("c")
			t12=ser.read(10)
			print "Temperatur12 in C: " +t12
			time.sleep(wait)		#zeit zm warten


			###IN DATEI temps.txt SCHREIBEN#####
			time.sleep(wait)
			str1=str(t1)
			str2=str(t2)
			str3=str(t3)
			str4=str(t4)
			str5=str(t5)
			str6=str(t6)
			str7=str(t7)
			str8=str(t8)
			str9=str(t9)
			str10=str(t10)
			str11=str(t11)
			str12=str(t12)
			localtime=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			print(localtime)
			newstr= ",".join((localtime,str1,str2,str3,str4,str5,str6,str7,str8,str9,str10,str11,str12))

			print newstr
			print "In Datei temps.txt speichern"
			fo=open("temps.txt","a+")
			fo.write(newstr)
			fo.write("\n")
			fo.write("\r")
			fo.close()
			end=timer()
			elapsedtime=end-start
			print("time elapsed: ")+str(elapsedtime)
			time.sleep(60-elapsedtime)