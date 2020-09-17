from tests.model.login import login, logout
from tests.config import USER_DETAILS


def test_login():
    login(email=USER_DETAILS['email'], password=USER_DETAILS['password'])


def test_logout():
    logout()
