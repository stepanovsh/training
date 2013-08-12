requirements:
	@echo "Installing requirements"
	@pip install -r requirements.txt

db:
	python manage.py syncdb --settings=training.settings.local

run:
	python manage.py runserver --settings=training.settings.local

collectstatic:
        python manage.py collectstatic --settings=training.settings.local


default:
	@make requirements
	@make db
	@make run

