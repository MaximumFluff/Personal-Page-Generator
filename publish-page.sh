#!/bin/bash

echo "Publishing page now..."

# Absolute directory for generated output git repo, which will be used for static site hosting on Cloudflare
directory="/home/alex/Documents/Personal-Page"
timestamp=$(date '+%d-%m-%Y %H:%M:%S')

if [ ! -d "$directory" ]
then
  echo "Output directory does not exist, creating now..."
fi

# Copy entire contents of generated personal page to output git folder
cp -a /home/alex/Documents/Personal-Page-Generator/public/. "$directory"

cd "$directory"

git add *

git commit -m "Published latest version of personal page: $timestamp"

git push origin main

if [ $? -eq 0 ]
then
  echo "Page published now!"
else
  echo "An error was encountered"
fi

# TODO: Better error handling
# TODO: Include page generation step before committing to output repo
