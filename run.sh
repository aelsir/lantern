source ./venv/bin/activate
git pull
pip install -r requirement.txt
python manage.py makemigrations
python manage.py migrate