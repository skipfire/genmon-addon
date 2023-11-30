~/genmon/startgenmon.sh stop
systemctl stop CaptivePortal
source ./venv/bin/activate
python HatTester.py
deactivate
systemctl start CaptivePortal
~/genmon/startgenmon.sh start
