#!/bin/bash 
whois google.com | grep -E "Registrant|Admin|Tech" > google.com.csv
