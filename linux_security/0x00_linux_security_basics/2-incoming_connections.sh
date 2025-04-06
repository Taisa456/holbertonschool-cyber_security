#!/bin/bash
sudo ufw allow 80/tcp && sudo ufw default deny incoming && sudo ufw enable && echo "Rules updated"
