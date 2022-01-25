#!/usr/bin/env bash

# VERY IMPORTANT! Strict mode. See: http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -euo pipefail
IFS=$'\n\t'

source project.conf

touch "${PORT}" || {
  echo "Port check failed!"
  echo "- You may want to replug your device."
  echo "- Confirm that your configured port, (${PORT}), is correct. "
  echo "Available ACM ports include: $(ls /dev/ttyACM*)"
  echo "(You can change this setting in 'project.conf')"
  exit 1
} && {
  echo "Using port: ${PORT}"
}
