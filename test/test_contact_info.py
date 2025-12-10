import re
from conftest import app
from random import randrange
from model.contact import Contact


# def test_phones_on_home_page(app):
#     contact_from_home_page = app.contact.get_contact_list()[0]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
#
# def test_phones_on_home_page_random(app):
#     contacts = app.contact.get_contact_list()
#     index = randrange(len(contacts))
#     contact_from_home_page = app.contact.get_contact_list()[index]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#     assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
#
# def test_emails_on_home_page(app):
#     contact_from_home_page = app.contact.get_contact_list()[0]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
#
# def test_phones_on_view_page(app):
#     contacts = app.contact.get_contact_list()
#     index = randrange(len(contacts))
#     contact_from_view_page = app.contact.get_contact_info_from_view_page(index)
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#     assert contact_from_view_page.home == contact_from_edit_page.home
#     assert contact_from_view_page.work == contact_from_edit_page.work
#     assert contact_from_view_page.mobile == contact_from_edit_page.mobile
#
def test_contact_info_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Testusertoinfo"))
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def test_contacts_info_on_home_page_db(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="Testusertoinfo"))
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    for i in range(len(contacts_from_db)):
        assert contacts_from_home_page[i].firstname == contacts_from_db[i].firstname
        assert contacts_from_home_page[i].lastname == contacts_from_db[i].lastname
        assert contacts_from_home_page[i].address == contacts_from_db[i].address
        assert contacts_from_home_page[i].all_emails_from_home_page == merge_emails_like_on_home_page(contacts_from_db[i])
        assert contacts_from_home_page[i].all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_db[i])
    # for contact in contacts_from_db:
    #     assert contact in contacts_from_home_page


def clear(s):
    return re.sub("[- ()]", "" , s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3])))