#!/usr/bin/env bash

# VERY IMPORTANT! Strict mode. See: http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -euo pipefail
IFS=$'\n\t'

source project.conf
source utils/check-port.sh

if utils/check-if-lib-updated.py; then
  echo "Pushing lib..."
  ampy --port "$PORT" put "lib" "$@"
fi

echo "Running ${FILE}..."
ampy --port "$PORT" run "$FILE" "$@"
echo "Done."