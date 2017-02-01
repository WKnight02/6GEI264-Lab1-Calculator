@echo off
for /f %%f in ('dir /b bin\*.py') do (python -m pydoc -w bin.%%f)
python -m pydoc -w bin
move *.html doc