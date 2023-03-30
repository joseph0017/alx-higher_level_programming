#!/bin/bash
# Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -s -X POST -F 'subject=I will always be here for PLD' -F 'email=test@gmail.com' "$1"
