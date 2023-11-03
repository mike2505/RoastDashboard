.PHONY: clean start init_migrations migrate upgrade insert downgrade show_migrations test install run

clean:
	find . -name "__pycache__" -exec rm -rf {} +
	find . -name "*.pyc" -exec rm -f {} +
	find . -name "*.pyo" -exec rm -f {} +
	find . -name "*~" -exec rm -f {} +
	find . -name ".cache" -exec rm -rf {} +

start:
	python3 run.py

init_migrations:
	FLASK_APP=run.py flask db init

migrate:
	FLASK_APP=run.py flask db migrate

upgrade:
	FLASK_APP=run.py flask db upgrade

downgrade:
	FLASK_APP=run.py flask db downgrade

show_migrations:
	FLASK_APP=run.py flask db show

insert:
	FLASK_APP=run.py flask insert-defaults

test:
	pytest

install:
	pip install -r requirements.txt

run:
	FLASK_APP=run.py FLASK_ENV=development flask run