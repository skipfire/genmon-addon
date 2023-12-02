#sudo pip install pyserial w1thermsensor
import RPi.GPIO as GPIO
import os
import serial
import sys
import time
from w1thermsensor import W1ThermSensor

sensorFound = False
blueIo = 7
blueNanoPiIo = 11
redIo = 24
greenIo = 23
buttonIo = 10
fanIo = 9

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(buttonIo, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(redIo,GPIO.OUT)
GPIO.setup(greenIo,GPIO.OUT)
GPIO.setup(blueIo,GPIO.OUT)
GPIO.setup(blueNanoPiIo,GPIO.OUT)
GPIO.setup(fanIo,GPIO.OUT)
GPIO.output(fanIo,GPIO.LOW)
GPIO.output(redIo,GPIO.LOW)
GPIO.output(greenIo,GPIO.LOW)
GPIO.output(blueIo,GPIO.LOW)

GPIO.output(redIo,GPIO.HIGH)
buttonTested = False

for sensor in W1ThermSensor.get_available_sensors():
    print("Temperature sensor found")
    sensorFound = True
if not sensorFound:
    print("Temperature sensor not found")
    GPIO.output(blueIo,GPIO.HIGH)

def buttonPressed(channel):
    global buttonTested
    GPIO.output(blueIo,GPIO.HIGH)
    GPIO.output(blueNanoPiIo,GPIO.HIGH)
    GPIO.output(redIo,GPIO.LOW)
    GPIO.output(fanIo, GPIO.HIGH)
    print("Button success")
    buttonTested = True
    time.sleep(1.5)

#From GenMon OtherApps/serialtest.py
def OpenSerialPort(name, rate):

    time.sleep(1.5)
    #Starting serial connection
    NewSerialPort = serial.Serial()
    NewSerialPort.port = name
    NewSerialPort.baudrate = rate
    NewSerialPort.bytesize = serial.EIGHTBITS     #number of bits per bytes
    NewSerialPort.parity = serial.PARITY_NONE     #set parity check: no parity
    NewSerialPort.stopbits = serial.STOPBITS_ONE  #number of stop bits
    NewSerialPort.timeout = 4                     #non-block read
    NewSerialPort.xonxoff = False                 #disable software flow control
    NewSerialPort.rtscts = False                  #disable hardware (RTS/CTS) flow control
    NewSerialPort.dsrdtr = False                  #disable hardware (DSR/DTR) flow control
    NewSerialPort.writeTimeout = 2                #timeout for write

    #Check if port failed to open
    if (NewSerialPort.isOpen() == False):
        try:
            NewSerialPort.open()
            print( "Serial port opened")
        except Exception as e:
            print( "error open serial port: " + str(e))
            return 0
    else:
        print( "Serial port already open???")
        return 0

    NewSerialPort.flushInput() #flush input buffer, discarding all its contents
    NewSerialPort.flushOutput()#flush output buffer, aborting current output

    return NewSerialPort

#From GenMon OtherApps/serialtest.py
def GetErrorInfo():
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    lineno = exc_tb.tb_lineno
    return fname + ":" + str(lineno)


GPIO.add_event_detect(buttonIo, GPIO.FALLING, callback=buttonPressed)
print("Waiting for button...")
try:
    while buttonTested == False:
        time.sleep(1)
except KeyboardInterrupt:
    print("KeyboardInterrupt button wait")

try:
    device='/dev/serial0' if len(sys.argv)<2 else sys.argv[1]

    baudrate=9600

    print ("\nLoopback testing for serial port " + device + "...\n")

    #Starting serial connection
    serialPort = OpenSerialPort(device, baudrate)

    if (serialPort == 0):
        print ("Error opening Serial Port " + device)
        sys.exit(1)

    TestString = "Testing 1 2 3\n"

    print("write data: sent test string")
    serialPort.write(TestString.encode())
    time.sleep(.05)
    print("waiting to received data....")
    ReceivedString = serialPort.readline()

    GPIO.output(blueIo,GPIO.LOW)
    GPIO.output(blueNanoPiIo,GPIO.LOW)
    if TestString != ReceivedString.decode("UTF-8"):
        print("FAILED: Sent data does not match receive. Received %d bytes" % len(ReceivedString))
        GPIO.output(redIo,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(redIo,GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(redIo,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(redIo,GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(redIo,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(redIo,GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(redIo,GPIO.HIGH)
    else:
        print("PASSED! Loopback successful")
        GPIO.output(greenIo,GPIO.HIGH)
        time.sleep(1.5)
    serialPort.close()

except Exception as e1:
    print( "error communicating...: " + str(e1) + " " + GetErrorInfo())
except KeyboardInterrupt:
    print("KeyboardInterrupt serial test")
    
GPIO.output(redIo,GPIO.HIGH)
GPIO.output(greenIo,GPIO.HIGH)
GPIO.output(blueIo,GPIO.HIGH)
GPIO.output(blueNanoPiIo,GPIO.HIGH)
time.sleep(1.5)
GPIO.output(greenIo,GPIO.LOW)
GPIO.output(blueIo,GPIO.LOW)
GPIO.output(blueNanoPiIo,GPIO.LOW)
GPIO.output(redIo,GPIO.LOW)
GPIO.output(fanIo,GPIO.LOW)

print("Done")
