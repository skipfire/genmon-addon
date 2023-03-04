# genmon-addon
## Fan Manager setup
The fan manager service is setup on preloaded units that support it. To manually install it elsewhere, log into your Pi with ssh or open a terminal in the OS UI, then run the following commands.  THe first two simply download the files, the third command moves the service definition to the appropriate folder, and the last two lines enable and start the fan service.
```
wget https://raw.githubusercontent.com/skipfire/genmon-addon/main/PintSizeFanManager.py
wget https://raw.githubusercontent.com/skipfire/genmon-addon/main/PintSizeFanManager.service
sudo mv ~/PintSizeFanManager.service /etc/systemd/system/
sudo systemctl enable PintSizeFanManager.service
sudo systemctl start PintSizeFanManager.service
```
The temperature the fan activates at can be changed PintSizeFanManager.py, just change the number on the 5th line to whatever temperature you want. If you want it to activate at 50°C (122°F), you would make that line of code look like:
```
onTemp = 50 #Temperature in celcius
``` 
The code is set to turn off the fan once the CPU is at least 1 degree below the activation temp.
