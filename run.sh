git pull
pip install -r requirement.txt
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --clear
python manage.py runserver 7000
