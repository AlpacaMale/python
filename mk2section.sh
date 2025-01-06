#!/bin/bash

if [ $# -eq 1 ]; then
    folder_name="section_$1"
    mkdir $folder_name
    touch "${folder_name}/task.py"
else
    echo "Usage: $0 folder_number"
    exit 1
fi

exit 0