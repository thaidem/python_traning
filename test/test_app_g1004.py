# -*- coding: utf-8 -*-
from model.group import Group


def test_app_group(app):
    app.group.create(Group(name="ffgnghvnb", header="dgdffbxf", footer="dVSxvbcb"))
#    app.session.logout()


def test_app_emptygroup(app):
    app.group.create(Group(name="", header="", footer=""))
