#! /usr/bin/env bash
set -e

python app/initial_data.py

pytest $* app/tests/
