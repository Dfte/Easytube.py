#!/bin/bash

echo "Installing pip3"
apt-get install python3-pip

echo "Installing pytube library."
pip3 install pytube

echo "Installing libav-tools."
apt install libav-tools 

echo "Installing FFMPEG."
apt install ffmpeg
