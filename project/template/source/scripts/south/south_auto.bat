cd ../../
echo off
echo --------------------------------------------------
echo Create schema migration and apply it
echo --------------------------------------------------
python manage.py schemamigration web --auto
python manage.py migrate web