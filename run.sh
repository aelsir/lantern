git pull
pip install -r requirement.txt
python manage.py makemigrations
python manage.py migrate
Run python manage.py collectstatic --clear
