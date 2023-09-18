import pytest


@pytest.yield_fixture()
def browser_config():
    print("Browser launched")

    yield
    print("Browser closed")


def test_login_001(browser_config):
    print("Login Test 001 Passed")


def test_login002(browser_config):
    print("Login Test 002 Passed")