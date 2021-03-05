#!/bin/bash

while [ true ]; do

#echo $(cat /proc/net/dev | tail -n 4 | cut -d ' ' -f1,2)

TZ=UTC date -d@$(cat /proc/uptime | cut -d ' ' -f1) +'%j %T' #| awk '{print $1-1"d",$2}'

echo $(cat /sys/class/power_supply/BAT0/uevent | grep POWER_SUPPLY_CAPACITY=)

echo "Średnie obciążenie systemu w ciągu ostatniej minuty: $(cat /proc/loadavg | cut -d ' ' -f1)"
echo "Średnie obciążenie systemu w ciągu ostatnich pięciu minut: $(cat /proc/loadavg | cut -d ' ' -f2)"
echo "Średnie obciążenie systemu w ciągu ostatnich piętnastu minut: $(cat /proc/loadavg | cut -d ' ' -f3)"

sleep 1s
done

