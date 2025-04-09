#!/bin/bash 
whois "$1" | grep -E "Registrant|Admin|Tech" > output.csv
