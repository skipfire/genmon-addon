/bin/bash ./Common.sh

cd ~/genmon-addon/
git config --global --add safe.directory '*'

echo "Install Log2ram"
/bin/bash ~/genmon-addon/Setup/Log2Ram.sh

echo "Install PintSizeFanManager"
/bin/bash ~/genmon-addon/FanManager/Setup.sh

echo "Install CaptivePortal"
/bin/bash ~/genmon-addon/CaptivePortal/Setup.sh

echo "Install HatTester"
cd ~/genmon-addon/HatTester/
/bin/bash ~/genmon-addon/HatTester/Setup.sh

echo "Clone and install GenMon"
echo 'dtoverlay=w1-gpio' | sudo tee -a /boot/firmware/config.txt
cd ~/
git clone https://github.com/jgyates/genmon.git
cd ~/genmon
bash ./genmonmaint.sh -i -n

read -p "A reboot is required, do that now? [y/n]" -n 1 -r
if [[ $REPLY =~ ^[Yy]$ ]]
then
    sudo reboot
fi
