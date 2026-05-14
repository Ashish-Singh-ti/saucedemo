class BasePage:
    def __init__(self, page):
        self.page = page

    def click(self, locator):
        self.page.click(locator)

    def type(self, locator, text):
        element = self.page.locator(locator)
        element.fill(text)

    def get_text(self, locator):
        element = self.page.locator(locator)
        return element.inner_text()



