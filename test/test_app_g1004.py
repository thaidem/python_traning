# -*- coding: utf-8 -*-
from model.group import Group


def test_app_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="ffgnghvnb", header="dgdffbxf", footer="dVSxvbcb"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_app_emptygroup(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
