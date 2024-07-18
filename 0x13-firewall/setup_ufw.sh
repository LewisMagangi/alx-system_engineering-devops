#!/bin/bash

# Update package list and install ufw
sudo apt-get update
sudo apt-get install ufw -y

# Allow SSH
sudo ufw allow 22/tcp

# Allow HTTPS
sudo ufw allow 443/tcp

# Allow HTTP
sudo ufw allow 80/tcp

# Enable ufw with force
sudo ufw --force enable

# Show ufw status
sudo ufw status
