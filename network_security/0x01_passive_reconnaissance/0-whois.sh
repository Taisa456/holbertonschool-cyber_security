#!/bin/bash 
whois google.com | grep -E "Registrant|Admin|Tech" > output.csv
