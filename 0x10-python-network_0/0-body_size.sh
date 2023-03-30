#!/bin/bash
# Bash script that sends a request to a URL and displays body size
curl --write-out "%{size_download}\n" "$1" --silent
