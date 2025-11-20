# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(
        Contact(firstname="Mary", middlename="Ivanovna", lastname="Ivanovna", nickname="test_user_mary",
                title="test_user2", company="CBA", address="CBA city", home="CBA", mobile="7999000000",
                work="79980000000", fax="79970000000",
                email="test99@testtest.com", email2="test98@testtest.com", email3="test97@testtest.com",
                homepage="www.yaya.com", bday="22", bmonth="July", byear="1991", aday="19", amonth="April", ayear="2009"))
    app.session.logout()
