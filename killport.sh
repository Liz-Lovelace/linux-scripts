#!/bin/bash

# Check if a port number is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <port-number>"
    exit 1
fi

PORT=$1

# Find PID of the process using the specified port
PID=$(lsof -ti tcp:${PORT})

# Check if a PID was found
if [ -z "$PID" ]; then
    echo "No process found listening on port $PORT."
    exit 2
else
    # Kill the process
    kill $PID
    if [ $? -eq 0 ]; then
        echo "Process on port $PORT has been terminated."
    else
        echo "Failed to terminate process on port $PORT. You may need to run this script as root or check if the process exists."
    fi
fi

