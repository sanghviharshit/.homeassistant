#!/bin/bash

cd ~/.homeassistant
source /srv/homeassistant/bin/activate
hass --script check_config

git add .
git status
echo -n "Enter the Description for the Change: [Minor Edit] "
read CHANGE_MSG
CHANGE_MSG=${CHANGE_MSG:-Minor Edit}
git commit -m "${CHANGE_MSG}"
git push origin master

exit
