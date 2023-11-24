
# Holla Amigos !

Holla. In this repo, i try to build simple back-end API for creating tweets ( i mention it as Post ) using Python based environment.

## TECH STACK
APP 
- Python
- Flask
- PyJWT
- Prisma ORM
- Flask CORS

DB
- PostgreSQL

## AVAILABLE API
- User (Registration, Login, Profile)
- Post / Tweets (Get by id's profile, Create)
- Follow (Add following, Remove following)

## LOCAL INSTALATION

Clone this project using :
```
git clone https://github.com/RevoU-FSSE-2/Week-21-vaiosyndicates.git

```
Then install and create virtual environment using
```
pip install virtualenv
```

```
python3 -m venv env
```

After make the virtual environment, active it using
```
source env/bin/activate
```
Then install the dependencies
```
pip install -r requirements.txt
```

## DB MIGRATING
Make sure the PostgreSQL is running and can be use
And in your terminal using this command to create and migrate the database
```
prisma db push
```
And all tables will be created automatically

## DISCLAIMER
This project fortunately doesn't have live deployment yet and still have many bugs to fix
But i will attach the Postman collection, so you can make the api call


