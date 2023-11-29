import os
import sys

if os.getuid():
    sys.exit('You need root access to install!')

print("###################################")
print("##### Captive Portal Initial Setup  #####")
print("###################################")
print()
print()

os.system('apt install python3 python3-rpi.gpio python3-pip -y')
os.system('pip3 install flask pyopenssl')

os.system('cp /home/genmonpi/genmon-addon/CaptivePortal/libs/reset_device/static_files/hosts.conf /etc/NetworkManager/dnsmasq-shared.d/')
os.system('mkdir /etc/cron.captiveportal')
os.system('cp /home/genmonpi/genmon-addon/CaptivePortal/libs/reset_device/static_files/apclient_bootstrapper /etc/cron.captiveportal')
os.system('chmod +x /etc/cron.captiveportal/apclient_bootstrapper')
os.system('echo "# Captive Portal Startup" >> /etc/crontab')
os.system('echo "@reboot root run-parts /etc/cron.captiveportal/" >> /etc/crontab')

print()
print()
print("#####################################")
print("##### Captive Portal Setup Complete  #####")
print("#####################################")

print()
print()
reboot_ans = input("Initial setup is complete. A reboot is required, would you like to reboot now? [y/N]: ")
if reboot_ans.lower() == 'y':
	os.system('reboot')
