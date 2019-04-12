# -*- coding: utf-8 -*-
from model.group import Group


def test_app_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="ffgnghvnb", header="dgdffbxf", footer="dVSxvbcb"))
    app.session.logout()


def test_app_emptygroup(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
