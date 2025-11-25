# -*- coding: utf-8 -*-
from model.contact import Contact
from conftest import app


def test_modify_first_contact_all(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact_all(
        Contact("Mary", "Ivanovna", "Ivanovna", "test_user_mary",
                "test_user2", "CBA", "CBA city", "CBA", "7999000000",
                "79980000000", "79970000000",
                "test99@testtest.com","test98@testtest.com", "test97@testtest.com",
                "www.yaya.com", "22", "July", "1991", "19","April", "2009"))
    app.session.logout()


def test_modify_first_contact_phone(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact_phone()
    app.session.logout()


def test_modify_first_contact_lastname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact_lastname()
    app.session.logout()
