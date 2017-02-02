@echo off
python -m pydoc -w modules.calcCore
python -m pydoc -w modules.calcInterface
move *.html documentation > nul
