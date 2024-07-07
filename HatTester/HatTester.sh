~/genmon/startgenmon.sh stop
sudo systemctl stop LinuxConfigHelper
source ./venv/bin/activate
python /home/genmonpi/genmon-addon/HatTester/HatTester.py
deactivate
sudo systemctl start LinuxConfigHelper
~/genmon/startgenmon.sh start
