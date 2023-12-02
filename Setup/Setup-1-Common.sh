echo "Update & upgrade apt"
sudo apt update -y && sudo apt upgrade -y

echo "Install some common tools"
sudo apt install -y locales-all git i2c-tools cron nano
