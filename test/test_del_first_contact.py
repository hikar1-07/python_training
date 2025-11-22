from conftest import app


def test_delete_first_contact(app):
    app.contact.delete_first_contact()
