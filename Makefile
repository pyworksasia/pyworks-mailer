init:
	cp ./mailer/.env.sample ./mailer/.env

test:
	python -m pytest

build:
	python setup.py sdist

minify:
	htmlmin ./src/mailer/templates/$$template.html ./src/mailer/templates/$$template.minify.html