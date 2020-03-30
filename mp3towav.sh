#!/bin.sh
for i in "$1"/*.mp3
do
    sox "$i" "$1/../waves/$(basename -s .mp3 "$i").wav"
done
