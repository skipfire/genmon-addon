echo "Install Log2ram"
echo "deb http://packages.azlux.fr/debian/ buster main" | sudo tee /etc/apt/sources.list.d/azlux.list
wget -qO - https://azlux.fr/repo.gpg.key | sudo apt-key add -
sudo apt update -y
sudo apt install log2ram
sudo sed -i "s/SIZE=40M/SIZE=250M/g" /etc/log2ram.conf
sudo sed -i "s/LOG_DISK_SIZE=100M/LOG_DISK_SIZE=300M/g" /etc/log2ram.conf
# After reboot, Verify with `sudo df -h`, you should see a log2ram line pointing to /var/log. `sudo mount` can also be used and a line should be seen with `log2ram on /var/log type tmpfs...`

echo "Install PintSizeFanManager"
sudo mv /boot/firmware/PintSizeFanManager.py ~/
sudo mv /boot/firmware/PintSizeFanManager.service /etc/systemd/system/
sudo mv /boot/firmware/HatTester.sh ~/
sudo mv /boot/firmware/HatTester.py ~/
sudo chown genmonpi:genmonpi PintSizeFanManager.py
sudo chown genmonpi:genmonpi HatTester.sh
sudo chown genmonpi:genmonpi HatTester.py
sudo chmod +x ./HatTester.sh
sudo systemctl enable PintSizeFanManager.service
sudo systemctl start PintSizeFanManager.service

echo "Clone and install GenMon"
echo 'enable_uart=1' | sudo tee -a /boot/config.txt

git clone https://github.com/jgyates/genmon.git
cd genmon
bash ./genmonmaint.sh -i
# Install answers:
# Enter to download packages
# y and Enter to copy config files
# y and Enter to setup serial port
# y and Enter to start genmon on boot

sudo reboot