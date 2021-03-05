#!/bin/bash
IFS=$'\n'
path="$1"
files=$(find "$path" -type f)
for file in $files; do
	if file "$file" | grep -q text$; then
    	sed -i 's/a/A/g' $file # g - zmień wszystkie instancje
	fi
done