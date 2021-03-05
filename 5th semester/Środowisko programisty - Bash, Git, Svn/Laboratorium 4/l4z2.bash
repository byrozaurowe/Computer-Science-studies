#!/bin/bash

startRev="$1"
endRev="$2"

svn_dir="$3"

dir=${svn_dir%/}
dir="${dir##*/}"

git init "$dir"

cd "$dir"

git config user.name "Wiktoria Byra"
git config user.email "wiktoriabyra99@gmail.com"

for r in $(seq $startRev $endRev); do
    svn log -q -r "$r" "$svn_dir"
    if [ $? != "1" ]; then
        rm -rf *
        svn export --force -q "$svn_dir" -r "$r" "./"

        msg="$(svn log -r $r $svn_dir | tail -n +4 | head -n -2)"

        git add "./**/*"
        git commit -m "$msg"
    fi
done
