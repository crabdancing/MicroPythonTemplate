#!/usr/bin/env bash

# VERY IMPORTANT! Strict mode. See: http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -euo pipefail
IFS=$'\n\t'

source project.conf

potentially_useful_serials=$(find /dev/ -iname 'ttyACM*' -o -iname 'ttyUSB*')
touch "${PORT}" || {
  echo "Port check failed!"
  echo "- You may want to replug your device."
  echo "- Confirm that your configured port, (${PORT}), is correct. "
  echo "Available ports include: ${potentially_useful_serials}"
  echo "(You can change this setting in 'project.conf')"
  exit 1
} && {
  echo "Using port: ${PORT}"
}
