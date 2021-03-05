#!/bin/bash
IFS=$'\n'
path="$1"
files=$(find "$path" -type f)
words=$(
for file in $files; do
	if file "$file" | grep -q text$; then
    	tr '[A-Z] ' '[a-z]\n' < "$file" | grep -v "^$" # -v to negacja
	fi
done | sort -u)
for word in $words; do
	echo $word
	grep -i -H "\<$word\>" $files
done
		