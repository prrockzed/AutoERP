#!/bin/bash

type -P python3 >/dev/null 2>&1 && echo Python 3 is installed
python3 -m pip install selenium
