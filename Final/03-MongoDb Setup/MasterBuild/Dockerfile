# escape=`

#ARG WIN_VER="ltsc2019"

#FROM mcr.microsoft.com/windows/servercore:$WIN_VER

FROM microsoft/iis:latest

SHELL ["powershell"]



VOLUME C:/data/db C:/data/configdb

ADD mongo-init.js C:/data/mongo/
ADD mongo-init.js /docker-entrypoint-initdb.d/


COPY mongo-init.bat /docker-entrypoint-initdb.d/

EXPOSE 27017
EXPOSE 27018
EXPOSE 27019


