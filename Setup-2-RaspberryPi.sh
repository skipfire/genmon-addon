echo "Install Log2ram"
echo "deb [signed-by=/usr/share/keyrings/azlux-archive-keyring.gpg] http://packages.azlux.fr/debian/ bookworm main" | sudo tee /etc/apt/sources.list.d/azlux.list
sudo wget -O /usr/share/keyrings/azlux-archive-keyring.gpg  https://azlux.fr/repo.gpg
sudo apt update -y
sudo apt install log2ram
sudo sed -i "s/SIZE=40M/SIZE=250M/g" /etc/log2ram.conf
sudo sed -i "s/LOG_DISK_SIZE=100M/LOG_DISK_SIZE=300M/g" /etc/log2ram.conf
# After reboot, Verify with `sudo df -h`, you should see a log2ram line pointing to /var/log. `sudo mount` can also be used and a line should be seen with `log2ram on /var/log type tmpfs...`

echo "Install PintSizeFanManager"
sudo cp ~/genmon-addon/PintSizeFanManager.service /etc/systemd/system/
sudo systemctl enable PintSizeFanManager.service
sudo systemctl start PintSizeFanManager.service
sudo chmod +x ./genmon-addon/HatTester.sh

echo "Install CpativePortal"
sudo apt install python3-flask -y
sudo python ~/genmon-addon/CaptivePortal/setup.py
sudo cp ~/genmon-addon/CaptivePortal/libs/reset_device/static_files/hosts.conf /etc/NetworkManager/dnsmasq-shared.d/
sudo cp ~/genmon-addon/CaptivePortal.service /etc/systemd/system/
sudo systemctl enable CaptivePortal.service
sudo systemctl start CaptivePortal.service

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
