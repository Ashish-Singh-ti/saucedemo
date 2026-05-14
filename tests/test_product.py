from playwright.sync_api import expect


def test_add_product_to_cart(product_page):

    product_page.add_to_cart(["Sauce Labs Backpack", "Sauce Labs Bike Light"])

    expect(product_page.get_remove_button("Sauce Labs Bike Light")).to_be_visible()

    assert product_page.get_cart_count() == 2