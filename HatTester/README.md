# HatTester
The HAT tester script validates that the Pi with a HAT/pHAT is ready for use. This script is built assuming that it is on a pre-loaded unit, attempting to use this on your own image will require modifications. The tested functions include the button, tri-color LED, TTL chip, and the serial configuration of the OS. It does not verify any GenMon configuration, but if this works then the Pi OS and hardware are correctly setup and ready for GenMon.

# HatTester.sh vs HatTesterLegacy.sh
HatTester.sh is intended for use with Bookworm and is compatible with the last images we shipped.  HatTesterLegacy.sh is for use with Bullseye.  Bookworm is setup to require python virtual environments and requires a couple of extra steps that are not needed and will throw errors if used on Bullseye.

# Knowledge level
This guide is being written assuming you know virtually nothing and the guide will be step by step. This does assume you have already connected the Pi to your network, if you have not then stop and get that done first - or you can do this on the Pi with a keyboard and monitor.

# Hardware Prep for HAT/pHAT
This is intended for use with the HAT/pHAT. The script could be modified for use with USB or non Raspberry Pi devices, but it will likely not work with those as is.
1. Disconnect from the generator, both for data and power on the barrel plug. For safety you should be power by USB for this test. \
2. Determine how you will short the 2 data pins, if you are using the Loopback Tester it does this for you and it ensures data flows the right direction, but you can also use a piece of wire or the scissors on a small pocket knife work well.
3. Make sure you are able to access the button on the HAT/pHAT, view the tri-color LED, and if you don't have the loopback tester be able to short the pins when you press the button. You don't have to short the pins yet, but you can if you have a stable method of doing so.
4. The pins to short are the two on the right side of the top row. You will NOT use any pins on the bottom row for this, those pins are all for power.
5. Power up your Pi.

# Login (assuming you are not on the Pi)
First you need to log into the Pi. To do this open a command prompt (on Windows) or a terminal session (on Mac or Linux) and then execute the following command to establish an SSH connection.
```sh
ssh genmonpi@genmon
```
If this is your first time using SSH you may be prompted to accept the fingerprint, choose yes. \
You will be prompted for the password, the default is `raspberry`, but hopefully you changed it. \
After a successful login you will be promopted with 
```sh
genmonpi@genmon:~ $
```
You can copy and paste the following commands
```sh
cd genmon-addon/HatTester
./HatTester.sh
```
This will stop GenMon, check the onboard temperature sensor, and then turn the LED red. \
Before continuing you need to have the Loopback Tester in place, or your shorting method, once ready briefly press the button. \
The LED will hopefully quickly turn green, then blue, then white, then go off. Once the light is blue, white, or off you can stop shorting the data pins. \
If the test was successful you should have the following output.
```sh
genmonpi@genmon:~/genmon-addon/HatTester $ ./HatTester.sh
using binary: /home/genmonpi/genmon/genenv/bin/python
Stopping genmon python scripts
Stopping....
Stopping gentemp.py
Stopping genserv.py
Stopping genmon.py
Temperature sensor found
Waiting for button...
Button success

Loopback testing for serial port /dev/serial0...

Serial port opened
write data: sent test string
waiting to received data....
PASSED! Loopback successful
Done
using binary: /home/genmonpi/genmon/genenv/bin/python
Starting genmon python scripts
Starting....
Starting /home/genmonpi/genmon/genmon.py
Starting /home/genmonpi/genmon/genserv.py
Starting /home/genmonpi/genmon/addon/gentemp.py
```
If the test was not successful the green LED will be lit for about 5 seconds and be followed by 3 red blinks, white, then dark. You would see output similar to below.
```sh
genmonpi@genmon:~/genmon-addon/HatTester $ ./HatTester.sh
using binary: /home/genmonpi/genmon/genenv/bin/python
Stopping genmon python scripts
Stopping....
Stopping gentemp.py
Stopping genserv.py
Stopping genmon.py
Temperature sensor found
Waiting for button...
Button success

Loopback testing for serial port /dev/serial0...

Serial port opened
write data: sent test string
waiting to received data....
FAILED: Sent data does not match receive. Received 0 bytes
Done
using binary: /home/genmonpi/genmon/genenv/bin/python
Starting genmon python scripts
Starting....
Starting /home/genmonpi/genmon/genmon.py
Starting /home/genmonpi/genmon/genserv.py
Starting /home/genmonpi/genmon/addon/gentemp.py
```
The FAILED line indicates that the data sent was not received and indicates there is some sort of serial problem in this equipment, either hardware (Pi or HAT/pHAT) or OS configuration (this is most common). \
Once you are done, you can type `exit` to log out of the SSH connection.
