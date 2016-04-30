#!/bin/bash

clear
My_Time=`date +"%Y-%m-%d%H:%M:%S"`
echo "Current time is $My_Time"
echo

echo "Starting picture process"
echo
fswebcam -d /dev/video0 -r 640x480 --no-banner image.jpg

echo
echo "Starting Plate Detection"
echo
python plate_reader.py

echo
echo "Moving image to log folder"
mv image.jpg log/$My_Time.jpg
echo "Finished"
