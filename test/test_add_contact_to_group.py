# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="Testusertoadd"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name = "test group to add"))
    groups = db.get_group_list()
    group = random.choice(groups)
    contacts_not_in_group = db.get_contacts_not_in_group(group)
    if len(contacts_not_in_group) == 0:
        app.contact.create_contact(Contact(firstname="NewTestusertoadd"))
        contacts_not_in_group = db.get_contacts_not_in_group(group)
    contact = random.choice(contacts_not_in_group)
    old_contacts_in_group = db.get_contacts_in_group(group)
    app.contact.add_contact_to_group(group.id, contact.id)
    new_contacts_in_group = db.get_contacts_in_group(group)
    old_contacts_in_group.append(contact)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)

# TO-DO for test runs

def test_remove_contact_from_group_db(app):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="Testusertoremovefromgroup"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name = "test group to remove from"))
    groups = db.get_group_list()
    group = random.choice(groups)
    old_contacts_in_group = db.get_contacts_in_group(group)
    if len(old_contacts_in_group) == 0:
        selected_contact_to_add = random.choice(db.get_contact_list())
        app.contact.add_contact_to_group(group.id, selected_contact_to_add.id)
        old_contacts_in_group = db.get_contacts_in_group(group)
    selected_contact = random.choice(old_contacts_in_group)
    old_contacts_not_in_group = db.get_contacts_not_in_group(group)
    app.contact.remove_contact_from_group(group.id, selected_contact.id)
    old_contacts_in_group.remove(selected_contact)
    new_contacts_in_group = db.get_contacts_in_group(group)
    new_contacts_not_in_group = db.get_contacts_not_in_group(group)
    old_contacts_not_in_group.append(selected_contact)
    assert sorted(new_contacts_in_group, key=Contact.id_or_max) == sorted(old_contacts_in_group, key=Contact.id_or_max)
    assert sorted(old_contacts_not_in_group, key=Contact.id_or_max) == sorted(new_contacts_not_in_group, key=Contact.id_or_max)