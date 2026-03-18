#this is test case writing example

from app2 import validate_user

def test_valid_credentials():
    assert validate_user("admin", "admin123")=="Login successful"

def test_invalid_password():
    assert validate_user("admin", "wrongpass")=="Invalid credentials"

def test_empty_password():
    assert validate_user("user1", "")=="Username or password cannot be empty"

def test_short_password():
    assert validate_user("user1", "123")=="Password too short"

def test_case_sensitivity():
    assert validate_user("Admin", "admin123")=="Invalid credentials"