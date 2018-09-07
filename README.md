# RSOI project
[![Build Status](https://travis-ci.org/ElusiveSpirit/rsoi-project.svg?branch=master)](https://travis-ci.org/ElusiveSpirit/rsoi-project)  
[Server link](https://glacial-temple-53481.herokuapp.com/)

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