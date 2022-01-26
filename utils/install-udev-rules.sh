#!/usr/bin/env bash

# VERY IMPORTANT! Strict mode. See: http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -euo pipefail
IFS=$'\n\t'

FILE_NUMBER=${FILE_NUMBER:-00}

sudo cp teensy.rules  "/etc/udev/rules.d/${FILE_NUMBER}-teensy.rules" -v
sudo udevadm control --reload-rules
