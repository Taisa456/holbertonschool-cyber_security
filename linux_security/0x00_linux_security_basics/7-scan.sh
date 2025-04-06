#!/bin/bash

# Check if an argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <subnetwork or domain>"
  exit 1
fi

# Perform the nmap scan
echo "Starting Nmap scan on $1..."
nmap -sn "$1"
