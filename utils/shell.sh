#!/usr/bin/env bash

# VERY IMPORTANT! Strict mode. See: http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -euo pipefail
IFS=$'\n\t'

source project.conf
source utils/check-port.sh

pio device monitor -b 115200 -p "$PORT" --raw "$@"
