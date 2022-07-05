# python3-template
Template to set up a basic Python3 based application

It takes care of the following:
- Provide a canary unittest
- Provide a git pre-commit hook to enforce style and execute unittests
- Provide a setup.bash script to setup a virtual environment and the pre-commit
  hook
- Provide .vscode launch.json and local settings.json

See [pyproject.toml](pyproject.toml) for used packages.
