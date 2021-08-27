#! /usr/bin/env bash

# Remove handytech timer and service.
if systemctl list-units --full --all | grep -Fq "handytech.timer"; then
    echo Removing service...
    sudo systemctl stop handytech.timer 
    sudo systemctl disable handytech.timer 
    sudo rm -v /lib/systemd/system/handytech.timer
    sudo rm -v /lib/systemd/system/handytech.service
    sudo systemctl daemon-reload
    sudo systemctl reset-failed
fi
