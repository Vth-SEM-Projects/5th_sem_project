# Final-Project
Alumni Database System
<pre> Frontend and databases are connected to the server
The following are the commands to be executed (Here _ before and after a word refers to name which can be used preferably)

Django

in cmd 
	1st time (in prefered directory)(install python)
		> mkvirtualenv _env_
		> pip install django
		> django-admin --versions
		> mkdir _dbms_project_
		> cd _dbms_project_
		> django-admin startproject _dbms_
		> cd _dbms_
		> python manage.py runserver
	next time
		> cd _dbms_project_
		> workon _env_
		> cd _dbms_
		> python manage.py runserver

In VSCode - only 1st time
	> python manage.py startapp _frontend_

Suppose CSS JS code are in static folder - only 1st time(After changes in settings.py)
	> python manage.py collectstatic 

Connect databases
	1st time - Install mysqlclient - refer https://youtu.be/QvzOG4C6Uy8
		in mysql
			> create database _project_db_;
			> use _project_db_;
		Note: In dbms folder-> settings.py -> in DATABASES update the name of database(here project_db), username and password of MySql.
		in VSCode
			> pip install Pillow
			> python manage.py makemigrations _frontend_
  				(If error: Authentication failed... then run the following command in mysql
  				> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '____'; )
			> python manage.py sqlmigrate _frontend_ 0001
			> python manage.py migrate
	next time
		> python manage.py sqlmigrate _frontend_ 0001(migration_file)
		> python manage.py migrate </pre>
