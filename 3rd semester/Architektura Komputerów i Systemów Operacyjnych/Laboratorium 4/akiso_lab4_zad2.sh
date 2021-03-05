#!/bin/bash

list=$(ls /proc/)
for pid in $list
do 
if [[ -d "/proc/$pid" && $pid =~ ^[0-9]+$ ]]; then
	cat /proc/$pid/status | grep Name
	cat /proc/$pid/status | grep Pid
	cat /proc/$pid/status | grep State
	count=$(ls /proc/$pid/fd | wc -l)
	echo "Liczba plików procesu: $count"
fi
done
