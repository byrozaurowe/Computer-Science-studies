#!/bin/bash
IFS=$'\n'
path="$1"
files=$(find "$path" -type f)
for file in $files; do
	if file "$file" | grep -q text$; then
		cat $file | while read line; do
			num=$(echo $line | tr '[A-Z] ' '[a-z]\n' | grep -v "^$" | sort | uniq -d | wc -l)
			if [ $num -gt 0 ]; then
				echo "$file:$line"
			fi
		done
	fi
done