.PHONY: help run isort black flake pylint test


help:
	@echo "run: run the project locally"
	@echo "isort: adjust imports"
	@echo "black: format code"
	@echo "flake: lint the code"
	@echo "pylint: lint the code"
	@echo "test: run the tests"
	@echo "format: format code with isort, black, pylint, flake8"

run:
	uvicorn src.main.app:app --reload --env-file .env

isort:
	isort src

black:
	black src

flake:
	flake8 src

pylint:
	pylint src

test:
	pytest --cov --cov-config=.coveragerc --cov-report=html

format: isort black flake pylint
