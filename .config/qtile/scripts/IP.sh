#!/bin/bash

echo "IP:$(ip address | grep "inet 12" | awk '{print $2}' )" 
