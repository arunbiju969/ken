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

REM Prompt for makemigrations
SET /P RUN_MAKEMIGRATIONS="Run makemigrations? (y/n): "
IF /I "%RUN_MAKEMIGRATIONS%"=="y" (
    echo Running makemigrations...
    python manage.py makemigrations
) ELSE (
    echo Skipping makemigrations...
)

REM Prompt for migrate
SET /P RUN_MIGRATE="Run migrate? (y/n): "
IF /I "%RUN_MIGRATE%"=="y" (
    echo Running migrate...
    python manage.py migrate
) ELSE (
    echo Skipping migrate...
)

REM Prompt for collectstatic
SET /P COLLECT_STATIC="Do you want to collect static files? (y/n): "
IF /I "%COLLECT_STATIC%"=="y" (
    python manage.py collectstatic --noinput
) ELSE (
    echo Skipping collectstatic...
)



REM Run the Django development server
python manage.py runserver

echo Done!
pause