cd ../../
echo --------------------------------------------------
echo Load saved dump into db
echo --------------------------------------------------
python manage.py reset --noinput auth contenttypes sites sessions web
python manage.py loaddata db/all.json