#!/bin/bash

function file_count_rows {
    if [[ ! -f $1 ]]; then
        echo "File not found!"
        exit 1
    fi
  
    rows=$(cat $1 | wc -l)
    # Subtract 1 from the row count to exclude the header row
    num_rows=$(expr $rows - 1)
    echo $num_rows
}

num_rows=$(file_count_rows $1)
echo "The number of rows in <$1>: $num_rows"