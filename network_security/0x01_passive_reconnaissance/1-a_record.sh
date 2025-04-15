#!/bin/bash
DOMAIN=$1
nslookup -type=A "$DOMAIN" 
