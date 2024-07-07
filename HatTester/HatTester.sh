~/genmon/startgenmon.sh stop
sudo systemctl stop LinuxConfigHelper
print("LinuxConfigHelper stop")
source ./venv/bin/activate
python /home/genmonpi/genmon-addon/HatTester/HatTester.py
deactivate
print("LinuxConfigHelper start")
sudo systemctl start LinuxConfigHelper
~/genmon/startgenmon.sh start
