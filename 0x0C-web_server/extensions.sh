#!/bin/bash

# Check if the script is being run as root
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root" 
    exit 1
fi

# Update package lists
apt update

# Install dnsutils package
apt install -y dnsutils

# Check if installation was successful
if [ $? -eq 0 ]; then
    echo "Installation completed successfully"
else
    echo "Installation failed"
fi
