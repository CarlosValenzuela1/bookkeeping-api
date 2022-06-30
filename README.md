# Bookkeeping API
A small python program that receives X and returns Y.

## Contents
* [How to run](#how-to-run)
* [How to run tests](#how-to-run-tests)
* [Thoughts and Reflections](#thoughts-and-reflections)
* [To-do list](#to-do-list)


## How to run
Assuming that pipenv is already install in your machine
If not please follow instructions from here: https://pipenv.pypa.io/en/latest/install/
pip install --user pipenv
Make sure it's also added to your PATH

```
pipenv shell
pipenv install -r ./requirements.txt

export FLASK_APP=src/app.py
export FLASK_ENV=development
flask run
```

# DELETE THIS:
To create the Requirements Carlos
pipenv lock -r > requirements.txt
