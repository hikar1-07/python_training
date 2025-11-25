from model.group import Group
from conftest import app


def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "test group"))
    app.group.modify_first_group(Group(name="New group name"))

def test_modify_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "test group"))
    app.group.modify_first_group(Group(header="New group header"))

def test_modify_first_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "test group"))
    app.group.modify_first_group(Group(footer="New group footer"))