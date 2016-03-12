#!/bin/bash

echo "Making sure we have everything we need for the program..."
sudo apt-get update;
sudo apt-get upgrade;
udo apt-get install libav-tools git python3-picamera python3-ws4py;

echo -ne  "Once the program is running, type in ";
ifconfig  | grep 'inet addr:'| grep -v '127.0.0.1' | cut -d: -f2 | awk '{ print $1, ":8082"}';
echo "Into your browser.";
echo "Program is running...press ctrl + C to quit."
python3 server.py; 

