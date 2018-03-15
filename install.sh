#!/bin/bash

echo "Installing pytube library."
pip3 install pytube

echo "Installing libav-tools."
apt install libav-tools 

echo "Installing FFMPEG."
apt install ffmpeg
