run:
	python manage.py runserver

super:
	python manage.py createsuperuser

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

test:
	python manage.py test