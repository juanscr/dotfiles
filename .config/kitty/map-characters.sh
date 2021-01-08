#!/usr/bin/env bash

printf "\n# ====== Symbols Mapping ====== #\n" >> kitty.conf
python print-unicode.py >> kitty.conf
