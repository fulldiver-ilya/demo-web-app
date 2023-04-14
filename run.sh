#!/usr/bin/env bash

install() {
    python3 -m venv .venv

    source "$PWD"/.venv/bin/activate

    python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt
}

dev() {
    python3 src/main.py --debug
}

prod() {
    gunicorn --bind :5050 --threads 8 --timeout 0 \
        --chdir ./src main:app
}

case ${1:-install} in
    install) install ;;
    dev) dev ;;
    prod) prod ;;
    *) echo "$0: No command named '$1'" ;;
esac
