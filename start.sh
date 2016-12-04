#!/bin/sh

sleep 10
ntp-wait -v

JSON_CONFIG="/home/alice/ionozor/hf/Ionozor.json"
#BUS_CONFIG="/home/odroid/bolidozor/station/bus_config.py"

ulimit -c unlimited

cd ~/repos/data-uploader

if ! pidof -x dataUpload.py > /dev/null; then
	./dataUpload.py $JSON_CONFIG #> /dev/null &
fi

