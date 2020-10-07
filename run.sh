#!/bin/bash

for i in $(adb devices | grep "device$" | awk '{print $1}');
do
  echo "start: {$i}"
  udid=$i python3 main.py $1 &
done
