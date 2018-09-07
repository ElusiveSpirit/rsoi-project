FLAGS=

setup:
	pip install pipenv
	pipenv install --dev --three

activate:
	pipenv shell -c

test:
	pipenv run py.test -s -v $(FLAGS) ./tests/

run:
	pipenv run python -m app
