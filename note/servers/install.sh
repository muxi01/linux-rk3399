#!/bin/bash

if [ "$1" = "" ] ; then 
	echo "example:$0 <rootfs.dir>"
else
	if [ -d "$1" ] ; then 
		CUR_DIR=$(pwd)
	else
		echo "rootfs is not exsit"
	fi
fi