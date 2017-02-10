import serial
import time
import sys
import glob
import platform


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
plat=platform.system()
print plat

if not result:
	print "No Serialports available!"
	print "Press Ctrl+C to exit the program"
else:
	print "Available Serialports"
	print serial_ports()
	print
	if plat.startswith('Win'):
		port1=result[0]
		print "opening "+str(port1)
		ser = serial.Serial(port1,9600,timeout=1)
		time.sleep(2)
		print"Connected"
		while 1:
			print "Getting Data:"
			print
			ser.write("t")
			t=ser.read(10)
			#ser.write("p")
			#p=ser.read(20)
			#time.sleep(0.25)
			ser.write("h")
			h=ser.read(10)
			ser.write("d")
			d=ser.read(10)
			ser.write("s")
			s=ser.read(10)
			print "Temperature " + str(t)
			print "Humidity " + str(h)
			#print "Pressure " + str(p)
			print "direction " + str(d)
			print "speed " + str(s)
			print
			
			
			time.sleep(1)

			
		
		
		
		
		
		
		
		
		