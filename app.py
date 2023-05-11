from peewee import *

db = PostgresqlDatabase('contacts', user='banana', password='123',
                        host='localhost', port=5432)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Contacts(BaseModel):
    name = CharField()
    email = CharField()
    phone_number = BigIntegerField()

guess = int(input("1: Add Contact\n2: View Contacts\n3: Search contacts by name\nSelect one : "))
def function(guess):
    if guess == 1:
        name =input("Enter name: ")
        email =input("Enter email :")
        phone_number = int(input("Enter phone number :"))
        new_contact = Contacts(name=name, email=email, phone_number=phone_number)
        new_contact.save()
    elif guess == 2:
        contacts = Contacts.select()
        for contact in contacts: 
            print(contact.name, contact.email, contact.phone_number)
    else:
        search = input("A man needs a name :")
        contacts = Contacts.select().where(Contacts.name == search)
        for contact in contacts: 
            print(contact.name, contact.email, contact.phone_number)
function(guess)        
