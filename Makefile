dev:
	@python manage.py runserver localhost:8010

migrate:
	@python manage.py makemigrations
	@python manage.py migrate

createsuperuser:
	@python manage.py createsuperuser