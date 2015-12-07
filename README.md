# Poster

This is django application for saving movies posters in your database.


Installation:

You need to have virtualenv for project. If you don't have please [install it]
    (https://virtualenv.readthedocs.org/en/latest/installation.html).
Create your environment:
```
virtualenv poster
```
Go to the folder /poster/bin and activate environment:
```   
source activate
```
Download project files:
```   
git clone  https://github.com/SirBigG/poster.git
```
Go to the poster directory and install requirements:
```
pip install -r requirements.txt
```
And the last, you need settind database. This app work with PostgreSQL. Install postgreSQL and create database.
Then go to the project settings and in DATABASES change NAME(your database name), USER(owner of db), PASSWORD(his password) and your HOST(for example: 127.0.0.0). Then run django command:
```
./manage.py migrate
```
for creating tables in database.

Now your application is ready to go. Run:
```
./manage.py runserver
```

Thank you!!!
