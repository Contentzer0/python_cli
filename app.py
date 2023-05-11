from peewee import *

db = PostgresqlDatabase('people', user='banana', password='123',
                        host='localhost', port=5432)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Contacts(BaseModel):
    name = CharField()
    email = CharField()
    phone_number = BigIntegerField

guess = int(input("1: Add Contact\n2: View Contacts\n3: Search contacts by name"))

