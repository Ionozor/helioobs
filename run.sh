#!/bin/bash
cd /home/alice/helioobs/log
arecord -f S16_LE -c 2 -r 48000 -t raw -D hw:1,0 | sox -t raw -e signed-int -b 16 -c 1 -r 1 - -t raw -e float -b 32 -c 1 -r 1 - | ../obs | ../sort
