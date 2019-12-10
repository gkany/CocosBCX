# Base image
FROM ubuntu:16.04

# MAINTAINER
MAINTAINER test

# node run env
RUN \
    apt-get update && \
    apt-get install -y -q --no-install-recommends \
        autoconf cmake vim git libbz2-dev libdb++-dev libdb-dev libssl-dev openssl libreadline-dev libtool libcurl4-openssl-dev libboost-all-dev g++ \
        vim git python3.5 python3-pip python-pip \
        mongodb redis-server mysql-server \
    && apt-get clean 

WORKDIR /

VOLUME /temp

# port-can 
# service
EXPOSE 8041
EXPOSE 8048
EXPOSE 8049
EXPOSE 8050

# for test
EXPOSE 8045

#db
EXPOSE 3306
EXPOSE 6379
EXPOSE 27017


