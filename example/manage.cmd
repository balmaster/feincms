@echo off
call env/scripts/activate.bat
set PYTHONPATH=.
python manage.py %*

