for file in *
	do
	file2=$(echo "$file" | tr "A-Z" "a-z")
		if [ "$file2" != "$file" ]
		then
		mv -- "$file" "$file2"
		fi
done
