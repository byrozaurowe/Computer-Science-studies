#!/bin/bash
IFS=$'\n'
path="$1"
files=$(find "$path" -type f)
for file in $files; do
    tr '[A-Z] ' '[a-z]\n' < "$file" | sort -u | grep -v "^$" 
done | sort | uniq -c