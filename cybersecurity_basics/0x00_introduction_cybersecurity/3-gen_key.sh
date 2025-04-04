#!/bin/bash
# This script generates an RSA SSH key pair with a 4096-bit key size

if [ -z "$1" ]; then
    echo "Usage: $0 <key_name>"
    exit 1
fi

ssh-keygen -t rsa -b 4096 -f "$1" -N ""

echo "SSH key pair generated: $1 and $1.pub"
