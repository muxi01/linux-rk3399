#!/bin/bash

OTG_MODE="/sys/kernel/debug/usb/fe800000.usb/mode"

if [ "$1" = "host" ] || [ "$1" = "device" ] ;then
	echo "$1" > ${OTG_MODE}
	cat ${OTG_MODE}
fi



