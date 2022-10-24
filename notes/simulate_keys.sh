#!/bin/bash

i=0

winid=$(xdotool search "move_circle")
echo $winid

time=1e-2
sleep 1

while true; do

sleep $time
echo c$i 
echo c$i > ./current_value.txt
sleep $time
echo c#$i
echo c#$i > ./current_value.txt
sleep $time
echo d$i 
echo d$i  > ./current_value.txt
sleep $time
echo d#$i
echo d#$i > ./current_value.txt
sleep $time
echo e$i
echo e$i > ./current_value.txt
sleep $time
echo f$i
echo f$i > ./current_value.txt
sleep $time
echo f#$i
echo f#$i > ./current_value.txt
sleep $time
echo g$i
echo g$i > ./current_value.txt
sleep $time
echo g#$i
echo g#$i > ./current_value.txt
sleep $time
echo a$i
echo a$i > ./current_value.txt
sleep $time
echo a#$i
echo a#$i > ./current_value.txt
sleep $time
echo h$i
echo h$i > ./current_value.txt

i=$((i+1))

if [ "$i" = "10" ] ; then
i=0
fi

done
