# Docker!
## No support provided for virtualization
Virtualized setups are intended for advanced users that already know what they are doing with the technologies are feel they can figure it out on their own.  Support will NOT be provided for docker or genmon in a docker, these will be files that "work on my machine".

## In progress
This is not yet done. I'm hoping to add a silent install switch to Genmon's code supporting virtualized promptless installs. Once that is done I believe the docker file is just 2 lines away from working.

Until then, once the docker file finishes, enter the terminal and run the genmonmaint -i, choose no to copy files and setting up the Raspberry Pi serial port.  After it completes make sure that the serial tcp setting = true in the config, and then you should be able to start genmon in the container.
