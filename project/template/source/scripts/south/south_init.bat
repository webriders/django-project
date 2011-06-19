cd ../../
echo off
echo --------------------------------------------------
echo Init South control for not south-controlled app
echo --------------------------------------------------
python manage.py schemamigration web --initial
python manage.py migrate web
