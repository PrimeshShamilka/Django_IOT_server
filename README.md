# Django IOT server
A RESTFUL web service designed for iSeizure IoT device.

## How to run
### In linux,

- Clone this repository to your local machine
- Create a python virtual environment
``` 
    python -m venv ~/.virtualenvs/djangodev
    source ~/.virtualenvs/djangodev/bin/activate
```
- Install dependencies
```
    cd iSeizure
    pythom -m pip install -r requirements.txt
```
- Run the server
```
    cd iSeizure
    python manage.py runserver
```
