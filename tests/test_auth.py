import pytest

def test_valid_login(login_page, product_page):

    login_page.navigate_to_login_page()

    login_page.login("standard_user", "secret_sauce")

    assert product_page._TITLE.is_visible()

@pytest.mark.parametrize("username, password, expected_error", [
    ("", "", "Epic sadface: Username is required"),
    ("", "secret_sauce", "Epic sadface: Username is required"),
    ("standard_user", "", "Epic sadface: Password is required"),
    ("standard_user", "wrong_pwd",
     "Epic sadface: Username and password do not match any user in this service")
]
                         )
def test_invalid_login(login_page, product_page, username, password, expected_error):
    login_page.navigate_to_login_page()

    login_page.login(username, password)

    error_text = login_page.get_error_message()

    assert error_text == expected_error



