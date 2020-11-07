#!/bin/bash
inotifywait -m /home/agmui/Downloads -e moved_to |
    while read path action file; do
        if [[ "$file" =~ .*osz$ ]]; then # Does the file end with .xml?
            echo "$file" # If so, do your thing here!
            (cd /home/agmui/Downloads && mv "$file" /home/agmui/Games/osu/drive_c/osu/Songs)
            echo "moved $file"
        fi
    done
#(cd /home/agmui/Downloads && mv *.osz /home/agmui/Games/osu/drive_c/osu/Songs)
