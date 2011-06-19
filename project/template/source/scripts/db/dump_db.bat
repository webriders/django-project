cd ../../
echo --------------------------------------------------
echo Dump whole project data in json format
echo --------------------------------------------------
python manage.py dumpdata --format=json --indent=4 > db/all.json