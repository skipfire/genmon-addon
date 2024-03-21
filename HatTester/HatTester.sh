~/genmon/startgenmon.sh stop
sudo systemctl stop CaptivePortal
source ./venv/bin/activate
python /home/genmonpi/genmon-addon/HatTester/HatTester.py
deactivate
sudo systemctl start CaptivePortal
~/genmon/startgenmon.sh start
