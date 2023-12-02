# genmon-addon
## PintSize HAT Fan Manager setup (HATs v2.3 and up)
The fan manager service is installed on preloaded units that support it. To manually install it elsewhere, log into your Pi with ssh or open a terminal in the OS UI, then run the following commands.  The first two simply download the files, the third command moves the service definition to the appropriate folder, and the last two lines enable and start the fan service.  This first works with v2.3 HATs.
```
git clone https://github.com/skipfire/genmon-addon
```
If you are using a login other than genmonpi, you need to use nano to edit line 7 in PintSizeFanManager.service and change `genmonpi` to your username.
```
sudo cp ~/genmon-addon/FanManager/PintSizeFanManager.service /etc/systemd/system/
sudo systemctl enable PintSizeFanManager.service
sudo systemctl start PintSizeFanManager.service
```
The temperature the fan activates at can be changed PintSizeFanManager.py, just change the number on the 5th line to whatever temperature you want. If you want it to activate at 50°C (122°F), you would update that line of code to the following:
`onTemp = 50 #Temperature in celcius`. The code is set to turn off the fan once the CPU is at least 1 degree below the activation temp.  This code will not work on a non-Raspberry Pi as it uses the RPi.GPIO library.

## Running GenMon in Docker
We do not provide support for running in Docker, however we do have a starter dockerfile and docker-compose file in the docker folder.  This can be a great option when used with Serial over TCP.

## RAM Disk
* Images created after September 30th, 2023 have RAMDISK setup for /var/log/. This reduces wear and tear on the SD card, however can also result in lost log data in the event it does not shut off cleanly. Logs should be backed to the SD card daily and upon a clean shutdown.
* Guide for setting it up is at https://ostechnix.com/how-to-write-log-files-in-ram-using-log2ram-in-linux/.

## Hotspot WiFi Configuration
* Preloaded units can be preloaded with standard networking which requires configuring through the OS GUI or with a wpa_supplicant.conf file. Alternatively there is an image that has RaspiWiFi installed to great a WiFi hotspot to configure the Pi's WiFi.
* To activate the hotspot, press and hold the button on the HAT/pHAT for 5 seconds.  It will first turn RED as a warning, then it will turn WHITE when it is activating the hotspot.
* The hotspot will show up with a name of `config` and the key is `genmon00`.  Connect to it and then browse to http://genmon/ or http://10.42.0.1/ to configure.  It may take a moment for your device to fully connect to the endpoint. If the page is not found give it up to 2 minutes. Mobile devices may automatically drop the connection as it will not provide internet access.
* After you are done configuring your device, it is recommended that you reboot the device.

## OpenGenSet Open Source Intention
The current plan is to have OpenGenSet be open source, though with restricted licensing. Some resources, such as circuit digrams, will not be opened until things are complete, and we reserve the right to change our minds on it.  When OpenGenSet is open sourced, it will be placed in its own repository and a link will be placed in this readme.

## Files
* CaptivePortal - all the files for the CaptivePortal service supporting configuration of your Pi.
* docker - files supporting setting up a docker image for GenMon, primarily used with a serial-TCP bridge. This is based on Debian.
* ESP32 - contains the ESPHome device yaml file for OpenGenSet to be used in serial bridge mode.
* FanManager - the files for the fan manager.
* Genmon HAT 2.0 Instructions.pdf - instructions linked on the store site for installing the v2.0+ HATs, pHATs, and pre-loaded units.
* HatTester - the files used to test the generator HATs, pHATs, and toppers on a workbench.
* LICENSE.md - the license (currently MIT) for this project. We do ask, but not require, that any improvements to these files make their way back here.
* README.md - this file.
* Setup/Setup-1-Common.sh - This script calls apt update and upgrade, installs several packages that will be needed, and sets locale to the US.
* Setup/Setup-2-RaspberryPi.sh - This script is used to setup the pre-loaded units, then tests are run, an image created, compressed, and duplicated.
* Setup/Setup-2-VirtualizedForSerial.sh - This script can be used along with the Common to setup GenMon for Serial over TCP on Ubuntu.

## Contributions welcome
I welcome anyone contributing to the cause.
