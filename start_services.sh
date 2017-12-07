#!/bin/bash
echo "Let's get things going"
### startup docker containers detached ###
docker-compose -f docker/support_containers/docker-compose.yml up -d
sleep 10 # wait for mariadb to start up
### starup flask server in new terminal with same python virtualenv ###
venv_bin=$(echo $PATH | awk -F: '{print $1}') #you must run this script in a python virtualenv. That will set the first entry in your path to its bin
cd python/Strom
gnome-terminal --tab -e "bash --rcfile $venv_bin/activate -ci 'python -m strom.strom-api.api.server'"
cd ../..
sleep 2
### startup engine in background ###
echo "All aboard the Engine class!"
### start data pushing script ###
cd cli/data_poster
./post_data.sh