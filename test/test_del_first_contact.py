from conftest import app
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Testusertodelete"))
    app.contact.delete_first_contact()
