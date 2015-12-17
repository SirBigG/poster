# Poster

This is django application for saving movies posters in your database.


Installation:

######1 .  Download project files:
```   
git clone  https://github.com/SirBigG/poster.git
```
######2 .  Go to the poster directory and install requirements:
```
sudo python setup.py install
```
######3 .  And the last, you need settind database. This app work with PostgreSQL. Install postgreSQL and create database.
Then go to the project settings and in DATABASES change NAME(your database name), USER(owner of db), PASSWORD(his password) and your HOST(for example: 127.0.0.0). Then run django command:
```
./manage.py migrate
```
for creating tables in database.

###If you don't need install packages in your locale machine.
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
Then do 1-3 steps. In step 2 run:
```
python setup.py install
```


###Now your application is ready to go. Run:
```
./manage.py runserver
```

##Thank you!!!
