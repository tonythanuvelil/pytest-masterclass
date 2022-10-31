install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

format:
	black . --extend-exclude *.ipynb

lint:
	pylint --disable=R,C *.py

test:
	python -m pytest -vv --cov=main --cov=greeting tests
	python -m pytest --nbval notebook.ipynb # tests for jupyter notebook

all: install format lint test