~/genmon/startgenmon.sh stop
sudo systemctl stop CaptivePortal
python /home/genmonpi/genmon-addon/HatTester/HatTester.py
sudo systemctl start CaptivePortal
~/genmon/startgenmon.sh start
