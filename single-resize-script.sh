#!/bin/bash

#simple script for resizing images in all class directories
#also reformats everything from whatever to png
file_name=$1
if [ `ls $file_name 2> /dev/null | wc -l ` -gt 0 ]; then
  convert "$file_name" -resize 28x28\! "${file_name%.*}.png"
  file "$file_name"
  if [ ${file_name: -4} == ".jpg" ];then
     rm "$file_name"
  fi
fi

