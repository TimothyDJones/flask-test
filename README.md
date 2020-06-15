## Create Python virtual environment
```bash
mkvirtualenv _virtual_env_name_
```

## Install packages specified in `requirements.txt`
```bash
pip install -r requirements.txt
```

## MySQL Connector
Python 3 requires the use of MySQL Connector package for connecting to MySQL databases.
```bash
pip install mysql-connector-python
```
To specify the use of MySQL Connector with SQLAlchemy, use database URI setting like this:
```bash
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://flask_admin:flask_admin@localhost/bookmarks'
```
See [here](https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/) for details.

# References
[Build a CRUD Web App With Python and Flask](https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-one)

