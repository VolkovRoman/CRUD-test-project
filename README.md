# CRUD App
This is my first Django project.\
The program allows you to Create, Read, Update and Delete data from database.
## Technologies:
* Python 3.6
* Django 2.1.5
* PostgreSQL 11
* Pgadmin4
## How to use:
### Preparing:
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
```
sudo apt-get install pgadmin4
```
* After that you need to create database with these options:
```
host: localhost
port: 5432
name: postgres
password: 1(if you want to change it, go to settings.py first and change password in database section)

```
* Finally, run server using manage.py file like this:
```
python3 manage.py runserver
```
### Using:
* Go to browser and type: http://127.0.0.1:8000/
* You will see the list of your database objects(in the first launch you will see almost header "List of products")
* To create a new object in database, press **"New product"** button
* The product has 3 options: Description, Price and Quantity. Fill in the fields and press **"Save"** button
* Now you have 1 product in list. If you press on the product name, you will be returned to the previous page, where you can change properties and delete the product(**"Delete"** button).
* Then you create a lot of products, you can use search field to find desired product(search by description, to run search, press **"Submit"** button)