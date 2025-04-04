#!/bin/bash
echo "$(sha256sum "$1" | awk '{ print $1 }')" == "$2" && echo "ok" || echo "invalid"
