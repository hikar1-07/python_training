from model.group import Group


def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group("New name",
                                     "New header",
                                     "New footer"))
    app.session.logout()