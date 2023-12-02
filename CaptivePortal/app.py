import fileinput
from flask import Flask, render_template, request
import os
import RPi.GPIO as GPIO
import subprocess
import sys
import time
from threading import Thread

app = Flask(__name__)

green = 23
blue = 7
red = 24
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)

@app.route('/')
def index():
    wifi_ap_array = scan_wifi_networks()
    return render_template('app.html', wifi_ap_array = wifi_ap_array)

@app.route('/save_config', methods = ['GET', 'POST'])
def save_config():
    timezone = request.form['timezone']
    subprocess.run(['timedatectl', 'set-timezone', timezone])
    return timezone

@app.route('/save_credentials', methods = ['GET', 'POST'])
def save_credentials():
    ssid = request.form['ssid']
    wifi_key = request.form['password']
    # Call ShutdownHotspot() in a thread otherwise the network change will prevent the response from getting to the browser
    def save_credentials_thread():
        time.sleep(2)
        ShutdownHotspot(ssid, wifi_key)
    t = Thread(target=save_credentials_thread)
    t.start()
    return ssid

@app.route('/update', methods = ['GET', 'POST'])
def update():
    ps = subprocess.Popen("GIT_DIR=/home/genmonpi/genmon-addon/.git git config --global --add safe.directory '*'",shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    output = ps.communicate()[0]
    ps = subprocess.Popen("GIT_DIR=/home/genmonpi/genmon-addon/.git git fetch origin",shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    output = output + ps.communicate()[0]
    ps = subprocess.Popen("GIT_DIR=/home/genmonpi/genmon-addon/.git git reset --hard origin/main",shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    output = output + ps.communicate()[0]
    subprocess.run(['chown', 'genmonpi:genmonpi', '/home/genmonpi/genmon-addon/.git/*'])
    subprocess.run(['chown', 'genmonpi:genmonpi', '/home/genmonpi/genmon-addon/.git/objects*'])
    def update_thread():
        time.sleep(2)
        subprocess.run(['systemctl', 'restart', 'CaptivePortal'])
        subprocess.run(['systemctl', 'restart', 'PintSizeFanManager'])
    t = Thread(target=update_thread)
    t.start()
    return output

@app.route('/stop_portal', methods = ['GET', 'POST'])
def stop_portal():
    def stop_portal_thread():
        time.sleep(2)
        subprocess.run(['systemctl', 'restart', 'CaptivePortal'])
    t = Thread(target=stop_portal_thread)
    t.start()
    return "Shutting down portal"

@app.route('/reboot', methods = ['GET', 'POST'])
def reboot():
    def rebootthread():
        time.sleep(2)
        os.system('reboot')
    GPIO.output(green, GPIO.LOW)
    GPIO.output(blue, GPIO.LOW)
    GPIO.output(red, GPIO.LOW)
    t = Thread(target=rebootthread)
    t.start()
    return "Rebooting"

def scan_wifi_networks():
    iwlist_raw = subprocess.Popen(['iwlist', 'scan'], stdout=subprocess.PIPE)
    ap_list, err = iwlist_raw.communicate()
    ap_array = []
    for line in ap_list.decode('utf-8').rsplit('\n'):
        if 'ESSID' in line:
            ap_ssid = line[27:-1]
            if ap_ssid != '':
                ap_array.append(ap_ssid)
    return ap_array

def ShutdownHotspot(ssid, wifi_key):
    GPIO.output(green, GPIO.LOW)
    GPIO.output(blue, GPIO.LOW)
    GPIO.output(red, GPIO.LOW)
    subprocess.run(['nmcli', 'dev', 'wifi', 'connect', ssid, 'password', wifi_key])
    subprocess.run(['systemctl', 'start', 'dnsmasq'])
    subprocess.run(['nmcli', 'conn', 'delete', 'id', 'Hotspot'])

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80)
