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

@app.route('/manual_ssid_entry')
def manual_ssid_entry():
    return render_template('manual_ssid_entry.html')

@app.route('/management')
def management():
    return render_template('management.html')

@app.route('/configure')
def configure():
    return render_template('configure.html')

@app.route('/save_config', methods = ['GET', 'POST'])
def save_config():
    timezone = request.form['dpdTimeZone']
    subprocess.run(['timedatectl', 'set-timezone', timezone])
    return render_template('save_config.html', timezone = timezone)

@app.route('/save_credentials', methods = ['GET', 'POST'])
def save_credentials():
    ssid = request.form['ssid']
    wifi_key = request.form['wifi_key']

    # Call set_ap_client_mode() in a thread otherwise the network change will prevent the response from getting to the browser
    def sleep_and_start_ap():
        time.sleep(2)
        set_ap_client_mode(ssid, wifi_key)
        
    t = Thread(target=sleep_and_start_ap)
    t.start()
    return render_template('save_credentials.html', ssid = ssid)

@app.route('/update', methods = ['GET', 'POST'])
def update():
    
    ps = subprocess.Popen("git pull",shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    output = ps.communicate()[0]
    subprocess.run(['chown', 'genmonpi:genmonpi', '.git/*'])
    subprocess.run(['chown', 'genmonpi:genmonpi', '.git/objects*'])
    return render_template('update.html', result = output)

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
    return render_template('reboot.html')

def scan_wifi_networks():
    iwlist_raw = subprocess.Popen(['iwlist', 'scan'], stdout=subprocess.PIPE)
    ap_list, err = iwlist_raw.communicate()
    ap_array = []

    for line in ap_list.decode('utf-8').rsplit('\n'):
        if 'ESSID' in line:
            ap_ssid = line[27:-1]
            if ap_ssid != '' and not ap_ssid.startswith("\x00"):
                ap_array.append(ap_ssid)

    return ap_array

def set_ap_client_mode(ssid, wifi_key):
    GPIO.output(green, GPIO.LOW)
    GPIO.output(blue, GPIO.LOW)
    GPIO.output(red, GPIO.LOW)
    subprocess.run(['nmcli', 'dev', 'wifi', 'connect', ssid, 'password', wifi_key])
    subprocess.run(['systemctl', 'start', 'dnsmasq'])
    subprocess.run(['nmcli', 'conn', 'delete', 'id', 'Hotspot'])

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80)
