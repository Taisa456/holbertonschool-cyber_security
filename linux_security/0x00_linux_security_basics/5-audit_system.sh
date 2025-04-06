#!/bin/bash

# Ensure you are running the script as a privileged user (root or sudoer)
if [ "$(id -u)" -ne 0 ]; then
  echo "This script must be run as root or with sudo privileges."
  exit 1
fi

# Run the Lynis audit
echo "Starting Lynis audit..."
sudo lynis audit system

# Provide feedback that the audit has completed
echo "System audit complete. Review the Lynis report for details."

# Optionally, display where the log and report files are saved
echo "Audit report can be found at /var/log/lynis-report.dat"

