# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.open_home_page_contact()
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(firstname="Ivan", middlename = "Ivanovich", lastname="Ivanov", nickname="test_user_ivan",
                    title="test_user", company="ABC", address="ABC city", home="ABC",  mobile="70000000000", work="71000000000", fax="72000000000",
                    email="test@testtest.com", email2="test2@testtest.com", email3="test3@testtest.com", homepage="www.ya.ru", bday="9", bmonth="July", byear="1970", aday="8", amonth="June", ayear="1999"))
    app.contact.return_to_contact_page()
    app.session.logout()


def test_add_empty_contact(app):
    app.open_home_page_contact()
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(firstname="", middlename = "", lastname="", nickname="",
                    title="", company="", address="", home="", mobile="", work="", fax="",
                    email="", email2="", email3="", homepage="", bday="", bmonth="-", byear="", aday="", amonth="-", ayear=""))
    app.contact.return_to_contact_page()
    app.session.logout()