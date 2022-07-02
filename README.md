#  Bookkeeping API

Python program to generate bookkeeping data for payments. The bookkeeping data is obtained from calculations done from an invoice.

##  Contents

*  [Pre-requisites](#pre-requisites)

*  [How to run application](#how-to-run-application)

*  [How to run tests](#how-to-run-tests)

*  [My thinking process](#my-thinking-process)


  ##  Pre-requisites

Please ensure that you have **Python 3.9+** and **pipenv** installed.

### Python
Python 3.9 is needed since the coding using one of its features (being able to use built-in collections types for type hinting, instead of having to import them).

More details can be found here:
[Python 3.9 Docs](https://docs.python.org/3/whatsnew/3.9.html#type-hinting-generics-in-standard-collections)

 ### Pipenv
If you don't have it installed, please follow the instructions from [here](https://pipenv.pypa.io/en/latest/install/).
```
pip install --user pipenv
```
*Make sure it's also added to your PATH*

##  How to run application

Assuming that pipenv and python 3.9+ are already install in your machine.
```
# Requirements installation and virtual environment creation
cd bookkeeping-api
pipenv install
pipenv shell

# Application execution
export FLASK_APP=src/app.py
export FLASK_ENV=development
flask run
```
Now you can send any json request from a file, go to the terminal and try this:
```
curl localhost:5000/bookkipping -d '@Example.json'
```
I provided an example.json file, in case you want to use it. It's located at the root of the repo.
No need to pass the  -H 'Content-Type: application/json' flag, since code is enforcing the json decoding within the code:
```
payload = request.get_json(force=True)
```

##  How to run tests

```
# Mostly tests for json validation
python -m src.tests.test_app 

# Mostly tests for each individual function
python -m src.tests.test_helpers 
```

# My thinking process
After reading the instructions a few times, I went ahead pen and paper to play around and find the relationship between the net_amount provided and the payments (amount) and invoice lines (unite_price_net).
I took the following notes:

- First get the invoice total (sum of all products) 
- Then, get each category total (sum of all products of the same category) 
- Then, get category percentage
- Then, create result of each category by applying the percentage to the payments total (do this for all payments)
- Then, round if needed

I tried to break the logic into small testable chunks, so I went ahead and created some tests to do TDD alongside with the actual code.

Have fun reviewing the code! and please let me know what can be improved or any other suggestions are appreciated.