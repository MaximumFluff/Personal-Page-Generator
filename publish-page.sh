# This script takes the generated output, copies it to a seperate git repo which is then published and used for static site hosting on Cloudflare

#!/bin/bash

# Absolute directory for generated files from creation script
generated_directory="/home/alex/Documents/Personal-Page-Generator"
# Absolute directory for generated output git repo
publish_directory="/home/alex/Documents/Personal-Page"
# Timestamp for git commit messages
timestamp=$(date '+%d-%m-%Y %H:%M:%S')

echo "Generating static files now..."
cd "$generated_directory"
uv run main.py

echo "Publishing page now..."
if [ ! -d "$publish_directory" ]
then
  # TODO: If output folder doesn't exist, instead clone it from Git
  echo "Output directory does not exist, creating now..."
fi

# Copy entire contents of generated personal page to output git folder
cp -a /home/alex/Documents/Personal-Page-Generator/public/. "$publish_directory"
cd "$publish_directory"
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
