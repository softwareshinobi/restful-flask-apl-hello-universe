#!/bin/bash

reset

clear

set -e 

set -x

# Define the API endpoint URL with root and path
API_URL="http://aventador.embanet.online:5000/process"

# Data to send in JSON format
DATA='{"string": "test", "num1": 10, "num2": 20}'

# Send POST request using curl with provided data
response=$(curl -s -X POST -H "Content-Type: application/json" -d "$DATA" $API_URL)

# Check for successful response (exit code 0) and extract the result
if [[ $? -eq 0 ]]; then
  result=$(echo $response | jq -r '.result')
  echo "API responded successfully with result: $result"
else
  echo "Error: API request failed!"
  exit 1
fi
