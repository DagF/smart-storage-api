# smart-storage-api


## Installation
`git clone git@github.com:trolllabs/2017-smart-storage-api.git`
`pip install virtualenv`
`virtualenv -p python3 env`
`. env/bin/active`
`pip install -r requirements.txt`

`cd src/smart-storage-api`
`cp local_settings_example.py local_settings.py`
` nano local_settings.py`
Delete one of the databases. If you want to use local database delete the sqlite3 one mysql one if not.


`python src/manage.py migrate`
`python src/manage.py createsuperuser`
`python src/manage.py runserver`