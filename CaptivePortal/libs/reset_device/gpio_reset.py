import RPi.GPIO as GPIO
import subprocess
import time

def reset_to_host_mode():
	subprocess.run(['systemctl', 'stop', 'dnsmasq'])
	subprocess.run(['nmcli', 'd', 'wifi', 'hotspot', 'ifname', 'wlan0', 'ssid', 'config', 'password', 'genmon00'])
	subprocess.run(['python', '/home/genmonpi/genmon-addon/CaptivePortal/libs/configuration_app/app.py'])
    
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

# This is the main logic loop waiting for a button to be pressed on GPIO 10 for 5 seconds.
# If that happens the device will reset to its AP Host mode allowing for reconfiguration on a new network.
while True:
    while GPIO.input(btn) == 0:
        counter = counter + 1
        GPIO.output(red, GPIO.HIGH)

        if counter == 5:
            GPIO.output(green, GPIO.HIGH)
            GPIO.output(blue, GPIO.HIGH)
            GPIO.output(red, GPIO.HIGH)
            counter = 0
            reset_to_host_mode()
        time.sleep(1) #sleep when button is pushed

    GPIO.output(green, GPIO.LOW)
    GPIO.output(blue, GPIO.LOW)
    GPIO.output(red, GPIO.LOW)
    counter = 0
    time.sleep(1) #sleep when button is not pushed
