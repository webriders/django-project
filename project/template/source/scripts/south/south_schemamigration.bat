cd ../../
echo off
echo --------------------------------------------------
echo Create schema migration
echo --------------------------------------------------
python manage.py schemamigration web --auto
