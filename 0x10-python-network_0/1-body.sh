#!/bin/bash
# sends a GET Request and displays a statuscode
curl -so /dev/null --write-out "%{http_code}\n" "$1"
