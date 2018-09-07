# RSOI project

## Requirements
 
 - pipenv
 - make

## Install
```bash
pipenv install
```

## Run application
```bash
make run
# or
pipenv run python -m app
```

## Test application
```bash
make test
# or
pipenv run py.test -s -v $(FLAGS) ./tests/
```