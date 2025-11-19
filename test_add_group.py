# -*- coding: utf-8 -*-
from group import Group
from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    # no step for open groups page
    app.create_group(Group(name="new_group_name", header="new_group_header", footer="new_group_footer"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    # no step for open groups page
    app.create_group(Group(name="", header="", footer=""))
    app.logout()