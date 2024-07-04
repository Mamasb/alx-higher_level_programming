#!/bin/bash

# Check if URL is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Assign the URL to a variable
URL="$1"

# Use curl to send a request to the URL and display the size of the response body in bytes
curl -so /dev/null "$URL" -w "%{size_download}\n"