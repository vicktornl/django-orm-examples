default: clean install format lint

clean:
	find . -name '*.pyc' -exec rm -rf {} +
	find . -name '__pycache__' -exec rm -rf {} +

install:
	pip3 install -r requirements_dev.txt

lint:
	black --check --diff .
	isort --check-only --diff .
	flake8 --ignore=E501 .

format:
	black .
	isort .
