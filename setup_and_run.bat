REM filepath: c:\Users\arunb\Documents\Project\Django\KEN\ken\setup_and_run.bat
@echo off
REM Move out one directory
cd ..

REM Activate the virtual environment
call .\env\Scripts\activate

REM Move back to the original directory
cd ken

REM Run the npx tailwindcss command in a new command prompt window
start cmd /k "npx @tailwindcss/cli -i ./static/src/input.css -o ./static/src/output.css --watch"

REM Run Django makemigrations and migrate commands
python manage.py makemigrations
python manage.py migrate

REM Run Django collectstatic command with no input prompt
python manage.py collectstatic --noinput

REM Run the Django development server
python manage.py runserver

echo Done!
pause