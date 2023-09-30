# GenMon-Addon
## PintSize HAT Fan Manager setup (HATs v2.3 and up)
The fan manager service is installed on preloaded units that support it. To manually install it elsewhere, log into your Pi with ssh or open a terminal in the OS UI, then run the following commands.  The first two simply download the files, the third command moves the service definition to the appropriate folder, and the last two lines enable and start the fan service.  This first works with v2.2 HATs.
```
wget https://raw.githubusercontent.com/skipfire/genmon-addon/main/PintSizeFanManager.py
wget https://raw.githubusercontent.com/skipfire/genmon-addon/main/PintSizeFanManager.service
sudo mv ~/PintSizeFanManager.service /etc/systemd/system/
sudo systemctl enable PintSizeFanManager.service
sudo systemctl start PintSizeFanManager.service
```
The temperature the fan activates at can be changed PintSizeFanManager.py, just change the number on the 5th line to whatever temperature you want. If you want it to activate at 50°C (122°F), you would update that line of code to the following:
`onTemp = 50 #Temperature in celcius`. The code is set to turn off the fan once the CPU is at least 1 degree below the activation temp.  This code will not work on a non-Raspberry Pi as it uses the RPi.GPIO library.

## Running GenMon in Docker
We do not provide support for running in Docker, however we do have a starter dockerfile and docker-compose file in the docker folder.  This can be a great option when used with Serial over TCP.

## Running Genmon on Ubuntu
Log into Ubuntu and execute `Setup-Ubuntu.sh` to install GenMon. After you run the script, genmon should start up and you can specify the IP and port of your serial bridge and setup any other security, notifications, or configuration.

## Files
* esphome-genmon-rs232-serialbridge.yml - the ESPHome device yaml file for OpenGenSet to be used in serial bridge mode.
* Genmon HAT 2.0 Instructions.pdf - instructions linked on the store site for installing the HATs, pHATs, and pre-loaded units.
* HatTester.py - the script used to test the generator HATs, pHATs, and toppers on a workbench.
* LICENSE.md - the license (currently MIT) for this project. We do ask, but not require, that any improvements to these files make their way back here.
* PintSizeFanManager.py - the fan manager service code.
* PintSizeFanManager.service - the fan manager service definition.
* README.md - this file.
* Setup-RaspberryPi.sh - This is the script used to setup for the pre-loaded units, then tests are run, an image created, compressed, and duplicated.
* Setup-Ubuntu.sh - GenMon configured for Serial over TCP on Ubuntu.

## RAM Disk
* Images created after September 30th, 2023 have RAMDISK setup for /var/log/. This reduces wear and tear on the SD card, however can also result in lost log data in the event it does not shut off cleanly. Logs should be backed to the SD card daily and upon a clean shutdown.
* Guide for setting it up is at https://ostechnix.com/how-to-write-log-files-in-ram-using-log2ram-in-linux/.

## Hotspot WiFi Configuration
* Preloaded units can be preloaded with standard networking which requires configuring through the OS GUI or with a wpa_supplicant.conf file. Alternatively there is an image that has RaspiWiFi installed to great a WiFi hotspot to configure the Pi's WiFi.
* The hotspot will show up with a name similar to `GenMon Config 1.0`.  Connect to it and then browse to http://10.0.0.1 to configure.
* For HATs v2.0 and higher, the button on the HAT is tied to a WiFi reset script. This will erase existing WiFi configs, reboot the device, and enable the hotspot to reconfigure.  To do this, hold the button for 5 seconds.  It will turn red as soon as you start pressing it, and then if you hold it for the 5 seconds it will turn white.  Release it upon it turning white and the Pi will reboot.
* The public RaspiWiFi repository has been forked for this project, the only differences are updates to the Readme.txt file and updates to have the reset script work with the button and tri-color LED on the PintSize.Me HATs.

## Contributions welcome
I welcome anyone contributing to the cause.

## OpenGenSet Open Source Intention
The current plan is to have OpenGenSet be open source, though with restricted licensing. Some resources, such as circuit digrams, will not be opened until things are complete, and we reserve the right to change our minds on it.  When OpenGenSet is open sourced, it will be placed in its own repository and a link will be placed in this readme.
