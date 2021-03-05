#!/bin/bash
adres=$(curl -s https://api.thecatapi.com/v1/images/search | jq '.[].url' | xargs)
curl -s $adres -o obrazek.jpg
catimg obrazek.jpg
rm obrazek.jpg
curl -s http://api.icndb.com/jokes/random | jq '.value.joke'