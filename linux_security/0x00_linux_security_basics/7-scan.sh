#!/bin/bash
nmap -sn "$1" || echo "Usage: $0 <subnetwork or domain>"
