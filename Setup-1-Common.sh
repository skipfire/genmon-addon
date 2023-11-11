echo "Update & upgrade apt"
sudo apt update -y && sudo apt upgrade -y

echo "Install some common tools"
sudo apt install -y locales-all git i2c-tools cron git nano

echo "Setup locale"
sudo sed -i "s/en_GB/en_US/g" /etc/default/locale
