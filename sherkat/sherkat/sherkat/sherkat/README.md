# how to run celery

* $ python manage.py runserver

* $ celery -A sherkat worker --loglevel=info

* $ celery -A sherkat beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler