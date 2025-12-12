#!/bin/bash

WATCHDOG_DEV="/dev/watchdog"

while true; do
	echo -n "1" > ${WATCHDOG_DEV}
	sleep 5
done
#
