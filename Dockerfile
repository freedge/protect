FROM groovy
USER root
RUN apt-get update ; \
    apt-get install -y build-essential iputils-ping bash

# got from http://public.dhe.ibm.com/storage/tivoli-storage-management/maintenance/client/v8r1/Linux/LinuxX86_DEB/BA/v818/
ADD 8.1.8.0-TIV-TSMBAC-LinuxX86_DEB.tar /

RUN dpkg -i /gskcrypt64_8.0-55.4.linux.x86_64.deb ; \
    dpkg -i /gskssl64_8.0-55.4.linux.x86_64.deb ; \
    dpkg -i /tivsm-api64.amd64.deb ; \
    dpkg -i /tivsm-ba.amd64.deb
    
# add the needed configuration files
ADD dsm.sys /opt/tivoli/tsm/client/ba/bin/dsm.sys
ADD dsm.opt /opt/tivoli/tsm/client/ba/bin/dsm.opt


ENTRYPOINT ["/usr/bin/dsmadmc"]
