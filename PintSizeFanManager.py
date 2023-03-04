import RPi.GPIO as GPIO
import os
import time

onTemp = 40 #Temperature in celcius

fanIo = 9
fanOn = False

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(fanIo,GPIO.OUT)
GPIO.output(fanIo,GPIO.LOW)

while True:
    cpu_temp = os.popen("vcgencmd measure_temp").readline()
    temp = float(cpu_temp.replace("temp=", "").replace("'C", ""))
    if fanOn and temp < (onTemp - 1):
        GPIO.output(fanIo,GPIO.LOW)
        fanOn = False
        print("Fan off")
    elif fanOn == False and temp >= onTemp:
        GPIO.output(fanIo,GPIO.HIGH)
        fanOn = True
        print("Fan on")
    time.sleep(15);
