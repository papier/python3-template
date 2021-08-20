#!/usr/bin/env bash
set -e

ln -sf ../../git_hooks/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit

python3.9 -m venv --prompt python-template .venv
source .venv/bin/activate
python3.9 -m pip install --upgrade pip
pip install --upgrade --upgrade-strategy eager -r requirements.txt
