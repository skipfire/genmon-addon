sudo apt install python3-flask -y
sudo cp ~/genmon-addon/CaptivePortal/hosts.conf /etc/NetworkManager/dnsmasq-shared.d/
sudo cp ~/genmon-addon/CaptivePortal/CaptivePortal.service /etc/systemd/system/
sudo systemctl enable CaptivePortal.service
sudo systemctl start CaptivePortal.service
