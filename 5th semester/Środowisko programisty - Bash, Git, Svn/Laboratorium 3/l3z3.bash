#!/bin/bash
IFS=$'\n'
rev="$1"
url="$2"
svn checkout -r $rev $url "temp_dir"
path=$(echo $PWD"/temp_dir")
files=$(find "$path" -type f)
for file in $files; do
    tr '[A-Z] ' '[a-z]\n' < "$file" | sort -u | grep -v "^$" 
done | sort | uniq -c