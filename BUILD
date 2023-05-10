#!/bin/bash

/home/verniy/.local/bin/pyside6-project build ./gui-design/gui-design.pyproject

mv gui-design/ui_*.py ./src/qtgui/view/ui/

pyinstaller ./src/main.py -y \
    --exclude-module PyQt5 \
    --exclude-module PyQt6 \

rm ./dist/main/libselinux.*
rm ./dist/main/libreadline.*
rm ./dist/main/libmount.*
rm ./dist/main/libcap.*
rm ./dist/main/libblkid.*