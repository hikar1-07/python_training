from model.group import Group
from conftest import app


def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "test group"))
    old_groups = app.group.get_group_list()
    group = Group(name="New group name")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_modify_first_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(header = "test group"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="New group header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#
# def test_modify_first_group_footer(app):
#     if app.group.count() == 0:
#         app.group.create(Group(footer = "test group"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(footer="New group footer"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)