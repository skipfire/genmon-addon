~/genmon/startgenmon.sh stop
sudo systemctl stop CaptivePortal
sudo systemctl stop PintSizeFanManager
source ./venv/bin/activate
python /home/genmonpi/genmon-addon/HatTester/HatTester.py
deactivate
sudo systemctl start CaptivePortal
sudo systemctl start PintSizeFanManager
~/genmon/startgenmon.sh start
