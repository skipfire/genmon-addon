# Docker!
## No support provided for virtualization
Virtualized setups are intended for advanced users that already know what they are doing with the technologies are feel they can figure it out on their own.  Support will NOT be provided for docker or genmon in a docker, these will be files that "work on my machine".

## In progress
Ignore the docker-compose, it is not ready.

This is not yet done. There is a pending PR to fix no-prompt installs, and genmon does not start automatically, but if `/git/genmon/startgenmon.sh start` is called from the terminal it does start correctly.

Preservation of configuration after refreshing the image is unknown, probably need to add some persistent volume definitions.

## Build & run
This will change once the docker file and docker-compose files are finished, but for the moment the following commands will build the container and start it up exposing port 8000.  This is just a for-now bit of documentation.
```
docker build . -t genmon
docker run -it -p 8000:8000 -d genmon /bin/bash
```

## Contributions welcome
I welcome anyone contributing to the cause.
