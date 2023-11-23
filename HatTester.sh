~/genmon/startgenmon.sh stop
source ./venv/bin/activate
python HatTester.py
deactivate
~/genmon/startgenmon.sh start
