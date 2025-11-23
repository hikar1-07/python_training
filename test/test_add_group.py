# -*- coding: utf-8 -*-
from model.group import Group
from conftest import app


def test_add_group(app):
    app.group.create(Group(name="new_group_name", header="new_group_header", footer="new_group_footer"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))