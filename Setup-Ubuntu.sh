sudo apt install cron git nano
cd genmon/
./genmonmaint.sh -i -n
sed -i 's/use_serial_tcp = False/use_serial_tcp = True/g' /etc/genmon/genmon.conf
./startgenmon.sh start