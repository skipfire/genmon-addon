# Making images with the Raspberry Pi Imager
In the Raspberry Pi imager:
* Pick either Bookworm GUI or Lite (Console only), 32-bit has better performance in the OS UI, especially if you are using a Pi Zero 2 or Pi 3.  64-bit works fine especially if you are not using the OS UI beyond initial setup of the device.
* Hostname: genmon
* Enable SSH checked, Use password authentication
* Set username and password checked
* Username: genmonpi
* Password: raspberry
* Setup WiFi details if you desire
* Timezone: it should default to your system's timezone, but just change it if not.
* Keyboard layout: us

After booting: 
* Change the password!
* Set WiFi country code
* Set boot mode to GUI or Console without automatic login
