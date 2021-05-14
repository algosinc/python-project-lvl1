install:
	poetry install

brain-games:
	poetry run brain-games

build: 
	poetry build

publish:
	poetry publish --dry-run

pinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 brain_games


