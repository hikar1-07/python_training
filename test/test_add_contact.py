# -*- coding: utf-8 -*-
from model.contact import Contact
from conftest import app
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits # +  " " * 10 string.punctuation +
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = ([Contact(firstname="",middlename= "", lastname="", nickname="", title="", company="", address="",
                     home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="")] +
            [Contact(firstname=random_string("firstname", 12),
                     middlename=random_string("middlename", 12),
                     lastname=random_string("lastname", 12),
                     nickname=random_string("nickname", 12),
                     title=random_string("title", 12),
                     company=random_string("company", 12),
                     address=random_string("address", 12),
                     mobile=random_string("mobile", 12),
                     home=random_string("home", 12),
                     work=random_string("work", 12),
                     fax=random_string("fax", 12),
                     email=random_string("email", 12),
                     email2=random_string("email2", 12),
                     email3=random_string("email3", 12),
                     homepage=random_string("homepage", 12))
                    # bday=random_string("bday", 2),
                    # bmonth=random_string("bmonth", 20),
                    # byear=random_string("byear", 20),
                    # aday=random_string("aday", 20),
                    # amonth=random_string("amonth", 20),
                    # ayear=random_string("ayear", 20))
                    for i in range(5)
             ])

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_add_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="test_user_ivan",
#                 title="test_user", company="ABC", address="ABC city", home="ABC", mobile="70000000000",
#                 work="71000000000", fax="72000000000",
#                 email="test@testtest.com", email2="test2@testtest.com", email3="test3@testtest.com",
#                 homepage="www.ya.ru", bday="9", bmonth="July", byear="1970", aday="8", amonth="June", ayear="1999")
#     app.contact.create_contact(contact)
#     assert len(old_contacts) + 1 == app.contact.count()
#     new_contacts = app.contact.get_contact_list()
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
#
# def test_add_empty_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(firstname="", middlename="", lastname="", nickname="",
#                 title="", company="", address="", home="", mobile="", work="", fax="", email="", email2="",
#                 email3="", homepage="", bday="", bmonth="-", byear="", aday="", amonth="-", ayear="")
#     app.contact.create_contact(contact)
#     assert len(old_contacts) + 1 == app.contact.count()
#     new_contacts = app.contact.get_contact_list()
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)