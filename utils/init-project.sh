#!/usr/bin/env bash

# VERY IMPORTANT! Strict mode. See: http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -euo pipefail
IFS=$'\n\t'

src='idea-template'
dst='.idea'
OLD_PROJECT_NAME=${OLD_PROJECT_NAME:-'MicroPythonTemplate'}
PROJECT_NAME=${PROJECT_NAME:-$(basename $(pwd))}

gio trash ${dst}/ || true
cp -ax ${src}/ ${dst}/ -v
grep -rl "${OLD_PROJECT_NAME}" ".idea/" | xargs sed -e "s/${OLD_PROJECT_NAME}/${PROJECT_NAME}/g" -i
mv -v "${dst}/${OLD_PROJECT_NAME}.iml" "${dst}/${PROJECT_NAME}.iml"
