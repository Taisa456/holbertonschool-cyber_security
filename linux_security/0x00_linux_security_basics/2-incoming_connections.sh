#!/bin/bash

# Set default incoming rule to deny
sudo ufw default deny incoming

# Allow incoming connections on port 80 (TCP)
sudo ufw allow 80/tcp

# Enable the firewall
sudo ufw enable

# Print a message confirming rules are updated
echo "Rules updated"

