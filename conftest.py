from idlelib import browser

import pytest
from playwright.sync_api import Playwright

from pages.loginpage import LoginPage
from pages.productspage import ProductPage



@pytest.fixture(scope="session")
def auth_state(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://saucedemo.com/")
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()
    page.wait_for_url("**/inventory.html")

    context.storage_state(path="auth_state.json")
    context.close()
    browser.close()
    return "auth_state.json"

@pytest.fixture
def logged_in_page(playwright, auth_state):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(storage_state=auth_state)
    page = context.new_page()
    page.goto("https://saucedemo.com/inventory.html")
    yield page
    context.close()
    browser.close()

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def product_page(logged_in_page):
    return ProductPage(logged_in_page)