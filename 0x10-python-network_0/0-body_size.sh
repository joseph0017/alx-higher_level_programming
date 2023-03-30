#!/bin/bash

HTTP_CODE=$(curl --write-out "%{size_download}" "$1" --silent)
echo $HTTP_CODE
