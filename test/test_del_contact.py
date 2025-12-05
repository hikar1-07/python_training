from conftest import app
from model.contact import Contact
from random import randrange
import random


# def test_delete_some_contact(app):
#     if app.contact.count() == 0:
#         app.contact.create_contact(Contact(firstname="Testusertodelete"))
#     old_contacts = app.contact.get_contact_list()
#     index = randrange(len(old_contacts))
#     app.contact.delete_contact_by_index(index)
#     assert len(old_contacts) - 1 == app.contact.count()
#     new_contacts = app.contact.get_contact_list()
#     old_contacts[index:index+1] = []
#     assert old_contacts == new_contacts

def test_delete_some_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Testusertodelete"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)