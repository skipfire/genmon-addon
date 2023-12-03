import RPi.GPIO as GPIO
import os
import time

onTemp = 60 #Temperature in Celsius

fanIo = 9
fanOn = False

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(fanIo,GPIO.OUT)
GPIO.output(fanIo,GPIO.LOW)

while True:
    cpu_temp = os.popen("vcgencmd measure_temp").readline()
    temp = float(cpu_temp.replace("temp=", "").replace("'C", ""))
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    if temp < (onTemp - 1):
        GPIO.output(fanIo,GPIO.LOW)
        if fanOn:
            fanOn = False
            print("Fan off")
    elif temp >= onTemp:
        GPIO.output(fanIo,GPIO.HIGH)
        if fanOn == False:
            fanOn = True
            print("Fan on")
    time.sleep(15);
