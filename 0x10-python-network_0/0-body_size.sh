#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response

HTTP_CODE=$(curl --write-out "%{size_download}" "$1" --silent)
echo $HTTP_CODE
