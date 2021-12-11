# setup
python manage.py runserver 127.0.0.1:8001 \ --settings=task2.settings

# task2.settings.py
If in production type DEBUG=False .
Then type ALLOWED_HOST=> type the host.
DATABASES=>change the database to sth elde then SQLite3
USE_TZ=True =>activate the timezones (datetime)
REST_FRAMEWORK=>configuration of api=> users can PUT,GET,DELETE and session users can onlu view

# TODO:
1.gitignore
2. signal to create valid/invalid measurement
3.recent (endpoint) from  valid measurements- in a sec, it is still locally
4.predict (endpoint) from  valid measurements- in a sec, it is still locally