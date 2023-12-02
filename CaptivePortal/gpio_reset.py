import RPi.GPIO as GPIO
import subprocess
import time

def ActivateHotspot():
    subprocess.run(['systemctl', 'stop', 'dnsmasq'])
    subprocess.run(['nmcli', 'd', 'wifi', 'hotspot', 'ifname', 'wlan0', 'ssid', 'config', 'password', 'genmon00'])
    ActivatePortal()

def ActivatePortal():
    subprocess.run(['python', '/home/genmonpi/genmon-addon/CaptivePortal/app.py'])

def buttonPressed(channel):
    global buttonCounter
    global buttonLastPress
    global portalUp
    if buttonCounter < 2:
        buttonLastPress = time.time()
        buttonCounter = buttonCounter + 1
        print("button pressed")
    else:
        buttonCounter = 0
        GPIO.output(green, GPIO.HIGH)
        GPIO.output(blue, GPIO.LOW)
        GPIO.output(red, GPIO.LOW)
        print("activating portal")
        portalUp = True
        print("portal up")
        ActivatePortal()
        portalUp = False
        print("portal down")

btn = 10
green = 23
blue = 7
red = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
GPIO.output(green, GPIO.LOW)
GPIO.output(blue, GPIO.LOW)
GPIO.output(red, GPIO.LOW)

counter = 0
buttonCounter = 0
buttonLastPress = time.time()
portalUp = False
GPIO.add_event_detect(btn, GPIO.FALLING, callback=buttonPressed)

# This is the main logic loop waiting for a button to be pressed on GPIO 10 for 5 seconds.
# If that happens the device will reset to its AP Host mode allowing for reconfiguration on a new network.
while True:
    if portalUp:
        continue
    while GPIO.input(btn) == 0:
        counter = counter + 1
        GPIO.output(red, GPIO.HIGH)

        if counter == 5:
            GPIO.output(green, GPIO.HIGH)
            GPIO.output(blue, GPIO.HIGH)
            GPIO.output(red, GPIO.HIGH)
            counter = 0
            ActivateHotspot()
        time.sleep(1) #sleep when button is pushed

    GPIO.output(green, GPIO.LOW)
    GPIO.output(blue, GPIO.LOW)
    GPIO.output(red, GPIO.LOW)
    counter = 0
    if buttonCounter > 0 and buttonLastPress + 1 < time.time():
        buttonCounter = 0
        print(buttonLastPress)
        print(time.time())
        print("reset button pressed due to time")
    time.sleep(1) #sleep when button is not pushed
