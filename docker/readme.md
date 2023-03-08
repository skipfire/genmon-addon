# Docker!
## No support provided for virtualization
Virtualized setups are intended for advanced users that already know what they are doing with the technologies are feel they can figure it out on their own.  Support will NOT be provided for docker or genmon in a docker, these will be files that "work on my machine".

## In progress
Ignore the docker-compose, it is not ready.

This is not yet done. I'm hoping to add a silent install switch to Genmon's code supporting virtualized promptless installs. Once that is done I believe the docker file is just 2 lines away from working.

Until then, once the docker file finishes, enter the terminal and run the genmonmaint -i, choose no to copy files and setting up the Raspberry Pi serial port.  After it completes make sure that the serial tcp setting = true in the config, and then you should be able to start genmon in the container.

## Build & run
This will change once the docker file and docker-compose files are finished, but for the moment the following commands will build the container and start it up exposing port 8000.  This is just a for-now bit of documentation.
```
docker build . -t genmon
docker run -it -p 8000:8000 -d genmon /bin/bash
```

## Contributions welcome
I welcome anyone contributing to the cause.
