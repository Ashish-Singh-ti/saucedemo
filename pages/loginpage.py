from pages.basepage import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._USERNAME = "[data-test='username']"
        self._PASSWORD = "[data-test='password']"
        self._LOGIN_BTN = page.locator("[data-test='login-button']")
        self._ERROR_MSG = "[data-test='error']"

    def navigate_to_login_page(self):
        self.page.goto("https://www.saucedemo.com")

    def login(self, user, pwd):
        self.type(self._USERNAME, user)
        self.type(self._PASSWORD, pwd)
        self._LOGIN_BTN.click()

    def get_error_message(self):
        error_text = self.get_text(self._ERROR_MSG)
        return error_text


