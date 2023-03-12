pecho "Install some common tools"
sudo apt install -y locales-all git i2c-tools
pip install w1thermsensor

echo "Setup locale"
sudo sed -i "s/en_GB/en_US/g" /etc/default/locale

echo "Setup keyboard"
sudo sed -i "s/gb/us/g" /etc/default/keyboard

echo "Update & upgrade apt"
sudo apt update -y
sudo apt upgrade -y

echo "Install PintSizeFanManager"
sudo mv /boot/PintSizeFanManager.py ~/
sudo mv /boot/PintSizeFanManager.service /etc/systemd/system/
sudo systemctl enable PintSizeFanManager.service
sudo systemctl start PintSizeFanManager.service
sudo chown genmonpi:genmonpi PintSizeFanManager.py
sudo chmod +x /boot/HatTester.sh

echo "Clone and install GenMon"
git clone https://github.com/jgyates/genmon.git
cd genmon
bash ./genmonmaint.sh -i

sudo reboot