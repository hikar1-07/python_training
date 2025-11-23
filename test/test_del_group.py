from conftest import app


def test_delete_first_group(app):
    app.group.delete_first_group()