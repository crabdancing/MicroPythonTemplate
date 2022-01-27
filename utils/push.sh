#!/usr/bin/env bash

# VERY IMPORTANT! Strict mode. See: http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -euo pipefail
IFS=$'\n\t'

source project.conf
source utils/check-port.sh

PROJECT_NAME=${PROJECT_NAME:-"$(basename "$(pwd)")"}


if utils/check-if-lib-updated.py; then
  lib_target=""
  cp -rv "lib/" /tmp/
  echo "Pushing lib..."
  ampy --port "$PORT" put "lib" "$@"
fi

echo "Pushing ${FILE}..."
ampy --port "$PORT" put "$FILE" "$@"
echo "Done."
