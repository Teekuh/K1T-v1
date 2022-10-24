#!/bin/bash

pid=$(pidof m2i)
kill -9 $pid

if [ -e /home/k1t/soul/toggle.txt ]; then	

	rm /home/k1t/soul/toggle.txt

fi
