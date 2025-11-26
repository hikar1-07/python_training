# -*- coding: utf-8 -*-
from model.contact import Contact
from conftest import app
from random import randrange


def test_modify_some_contact_all(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Testusertodelete"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact("Mary", "Ivanovna", "Ivanovna", "test_user_mary",
                "test_user2", "CBA", "CBA city", "CBA", "7999000000",
                "79980000000", "79970000000",
                "test99@testtest.com","test98@testtest.com", "test97@testtest.com",
                "www.yaya.com", "22", "July", "1991", "19","April", "2009")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_some_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Testusertodel"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    firstname = old_contacts[index].firstname
    modified_contact = Contact(lastname="Zukova-Testovskaya")
    modified_contact.id = old_contacts[index].id
    modified_contact.firstname = firstname
    app.contact.modify_contact_lastname(index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = modified_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_first_contact_phone(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Testusertodel"))
    app.contact.modify_first_contact_phone()

def test_modify_contact_email(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Testusertodel"))
    app.contact.modify_first_contact_all(Contact(email="test@ma-ilcom.ru"))

def test_modify_first_contact_email2(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Testusertodel"))
    app.contact.modify_first_contact_all(Contact(email2="test22@ma-ilcom.ru"))