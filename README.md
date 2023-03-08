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
The temperature the fan activates at can be changed PintSizeFanManager.py, just change the number on the 5th line to whatever temperature you want. If you want it to activate at 50°C (122°F), you would update that line of code to the following:
```
onTemp = 50 #Temperature in celcius
``` 
The code is set to turn off the fan once the CPU is at least 1 degree below the activation temp.

## Files
Genmon HAT 2.0 Instructions.pdf - instructions linked on the store site for installing the HATs, pHATs, and pre-loaded units.
HatTester.py - the script used to test the generator HATs, pHATs, and toppers on a workbench.
PintSizeFanManager.py - the fan manager service code
PintSizeFanManager.service - the fan manager service definition
README.md - this file
Setup.sh - This is the script used to setup for the pre-loaded units, then tests are run, an image created, compressed, and duplicated.
esphome-genmon-rs232-serialbridge.yml - the device yaml file for OpenGenSet to be used in serial bridge mode.

## Contributions welcome
I welcome anyone contributing to the cause.

## OpenGenSet Open Source Intention
The current plan is to have OpenGenSet be open source, though with restricted licensing. Some resources, such as circuit digrams, will not be opened until things are complete, and we reserve the right to change our minds on it.  When OpenGenSet is open sourced, it will be placed in its own repository and a link will be placed in this readme.
