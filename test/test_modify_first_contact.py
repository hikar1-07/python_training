# -*- coding: utf-8 -*-
from model.contact import Contact
from conftest import app


def test_modify_first_contact_all(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Testusertodelete"))
    app.contact.modify_first_contact_all(
        Contact("Mary", "Ivanovna", "Ivanovna", "test_user_mary",
                "test_user2", "CBA", "CBA city", "CBA", "7999000000",
                "79980000000", "79970000000",
                "test99@testtest.com","test98@testtest.com", "test97@testtest.com",
                "www.yaya.com", "22", "July", "1991", "19","April", "2009"))

def test_modify_first_contact_phone(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Testusertodel"))
    app.contact.modify_first_contact_phone()

def test_modify_first_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Testusertodel"))
    app.contact.modify_first_contact_lastname()

def test_modify_first_contact_email(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Testusertodel"))
    app.contact.modify_first_contact_all(Contact(email="test@ma-ilcom.ru"))

def test_modify_first_contact_email2(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Testusertodel"))
    app.contact.modify_first_contact_all(Contact(email2="test22@ma-ilcom.ru"))