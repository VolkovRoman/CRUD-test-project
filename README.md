# CRUD App
This is my first Django project.\
The program allows you to Create, Read, Update and Delete data from database.
## Technologies:
* Python 3.6
* Django 2.1.5
* PostgreSQL 11
* Pgadmin4
## How to use:
Preparing:\
* Install PostgreSQL 11
* At first run the commands below to add the repository key and the repository
```
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -sc)-pgdg main" > /etc/apt/sources.list.d/PostgreSQL.list'
```
* To install PostgreSQL 11, run the commands below
```
sudo apt update
sudo apt-get install postgresql-11
```
* Install pgAdmin4
```text
sudo apt-get install pgadmin4
```
* 