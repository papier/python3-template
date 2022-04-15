#!/usr/bin/env bash

# This script sets up the development environment.
set -e

# Setup local pre-commit git hook
ln -sf ../../git_hooks/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit

# Setup local virtual environment
python3.10 -m venv --prompt python-template .venv
# Install required packages into local virtual environment
source .venv/bin/activate
python3.10 -m pip install --upgrade pip
pip install --upgrade --upgrade-strategy eager -r requirements.txt
# This installs the project in develop mode
pip install --editable .
