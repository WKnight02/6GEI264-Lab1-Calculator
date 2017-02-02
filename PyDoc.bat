@echo off
python -m pydoc -w bin.calcCore
python -m pydoc -w bin.calcInterface
move *.html doc > nul
