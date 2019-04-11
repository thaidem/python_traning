# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_app_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="ffgnghvnb", header="dgdffbxf", footer="dVSxvbcb"))
    app.logout()


def test_app_emptygroup(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()