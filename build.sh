./setup.sh
pip3 install pyinstaller
pyinstaller -F --add-data "asset:asset" -n FieryDragons ./FieryDragons/src/fieryDragons/__main__.py


