#!/bin/bash

# Adds files of an extension 2 (i.e *.type) searching in path 1
git ls-files "$1" | grep "$2" | xargs git add
