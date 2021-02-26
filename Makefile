test:
	python -m pytest --pyargs src

build:
	python setup.py sdist

test-minify:
	htmlmin ./src/mailer/templates/order_created.html ./src/mailer/templates/order_created.minify.html