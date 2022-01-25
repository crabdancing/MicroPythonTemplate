#!/usr/bin/env bash

# VERY IMPORTANT! Strict mode. See: http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -euo pipefail
IFS=$'\n\t'

sudo cp 00-teensy.rules  /etc/udev/rules.d/ -v
sudo udevadm control --reload-rules
