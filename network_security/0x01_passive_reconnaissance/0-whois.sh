#!/bin/bash 
whois "$1" > temp.txt | echo "Registrant Information , Admin Information , Tech Information";
