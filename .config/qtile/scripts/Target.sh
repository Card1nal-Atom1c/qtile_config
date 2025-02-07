#!/bin/bash

ip_address=$(cat $HOME/.config/qtile/scripts/Target.txt | awk '{print $1}')
machine_name=$(cat $HOME/.config/qtile/scripts/Target.txt | awk '{print $2}')

if [ $ip_address ] && [ $machine_name ]; then
    echo "Target:$ip_address-$machine_name"
else
    echo "No Target"
fi
