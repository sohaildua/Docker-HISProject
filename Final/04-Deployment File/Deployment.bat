@ECHO OFF


docker create  --name deploytool microsoft/iis

docker cp Deployment deploytool:c:/deployment/
docker start deploytool
PAUSE