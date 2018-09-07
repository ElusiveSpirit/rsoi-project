FLAGS=

test:
	pipenv run py.test -s -v $(FLAGS) ./tests/

run:
	pipenv run python -m app
