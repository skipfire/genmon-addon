FROM python

RUN apt update -y
RUN apt upgrade -y

#The timezone specified here just bypasses some required configuration, it does not appear to be configuring a persistent setting.
RUN DEBIAN_FRONTEND="noninteractive" TZ="America/New_York" apt install -y sudo cron net-tools nano

EXPOSE 22
EXPOSE 443
EXPOSE 8000

RUN mkdir /git && cd /git && git clone http://github.com/jgyates/genmon.git

RUN cd /git/genmon && sudo chmod 775 startgenmon.sh && chmod 775 genmonmaint.sh

RUN /bin/bash /git/genmon/genmonmaint.sh -i -n
RUN /git/genmon/startgenmon.sh start

RUN sed -i 's/use_serial_tcp = False/use_serial_tcp = True/g' /etc/genmon/genmon.conf

CMD /git/genmon/startgenmon.sh start && tail -F /var/log/startup.log

#Build docker image with:
#docker build . -t genmon
#Start the docker instance with:
#docker run -it -p 8000:8000 -d genmon
