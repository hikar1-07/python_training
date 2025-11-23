# -*- coding: utf-8 -*-
from model.contact import Contact
from conftest import app


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="test_user_ivan",
                title="test_user", company="ABC", address="ABC city", home="ABC", mobile="70000000000",
                work="71000000000", fax="72000000000",
                email="test@testtest.com", email2="test2@testtest.com", email3="test3@testtest.com",
                homepage="www.ya.ru", bday="9", bmonth="July", byear="1970", aday="8", amonth="June", ayear="1999")
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="", middlename="", lastname="", nickname="",
                title="", company="", address="", home="", mobile="", work="", fax="", email="", email2="",
                email3="", homepage="", bday="", bmonth="-", byear="", aday="", amonth="-", ayear="")
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)