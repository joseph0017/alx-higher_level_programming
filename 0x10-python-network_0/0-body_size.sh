#!/bin/bash
# Bash script that sends a request to a URL and displays body size
curl -so --write-out '%{size_download}\n' "$1"
