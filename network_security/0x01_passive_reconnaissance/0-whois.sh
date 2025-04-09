#!/bin/bash 
whois "$1" > temp.txt | echo "Section,Name,Email,Org,Phone";
