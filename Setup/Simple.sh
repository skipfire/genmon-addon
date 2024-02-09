echo "Update & upgrade apt"
sudo apt update -y && sudo apt upgrade -y

echo "Install some common tools"
sudo apt install -y locales-all git i2c-tools cron nano

echo "Install Log2Ram"
echo "deb [signed-by=/usr/share/keyrings/azlux-archive-keyring.gpg] http://packages.azlux.fr/debian/ bookworm main" | sudo tee /etc/apt/sources.list.d/azlux.list
sudo wget -O /usr/share/keyrings/azlux-archive-keyring.gpg  https://azlux.fr/repo.gpg
sudo apt install log2ram
sudo sed -i "s/SIZE=40M/SIZE=250M/g" /etc/log2ram.conf
sudo sed -i "s/LOG_DISK_SIZE=100M/LOG_DISK_SIZE=300M/g" /etc/log2ram.conf
# After reboot, Verify with `sudo df -h`, you should see a log2ram line pointing to /var/log. `sudo mount` can also be used and a line should be seen with `log2ram on /var/log type tmpfs...`

echo "Clone and Install GenMon"
echo 'dtoverlay=w1-gpio' | sudo tee -a /boot/firmware/config.txt
git clone https://github.com/jgyates/genmon.git
cd ~/genmon
bash ./genmonmaint.sh -i -n
