#!/bin/bash
sudo nmap -sn "$1" || echo "Usage: $0 <subnetwork or domain>"
