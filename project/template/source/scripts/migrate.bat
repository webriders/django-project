cd ..
echo off
echo --------------------------------------------------
echo Migrate database
echo --------------------------------------------------
python manage.py schemamigration web --auto
python manage.py migrate web
