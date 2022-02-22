release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input
heroku config:set DISABLE_COLLECTSTATIC=1
web: gunicorn ICIVIDRF.wsgi