set -o errexit
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser --noinput
python manage.py collectstatic --noinput