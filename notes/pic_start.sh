#!/bin/bash

m2i -c /home/k1t/soul/config.lua -s /home/k1t/soul/basic.lua  &
sleep 5

#to do "aconnect 20:0 128", but undependant on the actual ports:
keyboard=$(aconnect -i |grep "CH345" |awk '{ print $2 }' |head -n 1)
midi2input=$(aconnect -i |grep "midi2input" |awk '{ print $2 }' |sed 's/.$//')
aconnect ${keyboard}0 ${midi2input}

python3 /home/k1t/soul/K1T.py &
