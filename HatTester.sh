~/genmon/startgenmon.sh stop
sudo systemctl stop CaptivePortal
source ./venv/bin/activate
python HatTester.py
deactivate
sudo systemctl start CaptivePortal
~/genmon/startgenmon.sh start
