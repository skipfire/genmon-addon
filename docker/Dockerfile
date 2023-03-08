FROM python

RUN apt update -y
RUN apt upgrade -y

#The timezone specified here just bypasses some required configuration, it is not configuring a persistent setting.
RUN DEBIAN_FRONTEND="noninteractive" TZ="America/New_York" apt install -y sudo cron net-tools nano

EXPOSE 22
#EXPOSE 443
EXPOSE 8000

RUN mkdir /git && cd /git && git clone https://github.com/jgyates/genmon.git

RUN cd /git/genmon && sudo chmod 775 startgenmon.sh && chmod 775 genmonmaint.sh

RUN /git/genmon/startgenmon.sh start
#RUN /git/genmon/genmonmaint.sh -id

RUN sed -i 's/use_serial_tcp = False/use_serial_tcp = True/g' /etc/genmon/genmon.conf

RUN /git/genmon/startgenmon.sh start

#docker build . -t genmon
#docker run -it -p 8000:8000 -d genmon /bin/bash
