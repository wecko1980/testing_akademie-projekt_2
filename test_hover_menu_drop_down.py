import pytest
from playwright.sync_api import sync_playwright

# vytvořím si instanci browser
@pytest.fixture()
def browser():
    with sync_playwright() as playwright:
        browser = playwright.firefox.launch(headless=False, slow_mo=2000)
        yield browser
        browser.close()

# vytvořím si page v nadefinovaném browseru
@pytest.fixture()
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

def test_hover_menu_drop_down(page):
    page.goto("https://engeto.cz/")
    
    # odkliknu nezbytné cookies
    refuse_button = page.locator("#cookiescript_reject")
    refuse_button.click()

    # najdu položku menu "Kurzy" a najedu na ní myší
    top_menu_item = page.locator("#top-menu .area-kurzy > a")
    top_menu_item.hover()
    
    # ověřím viditelnost drop down submenu, které se zobrazí po najetí na položku "Kurzy"
    drop_down_submenu = page.locator("#top-menu > li.area-kurzy > ul")
    drop_down_submenu.is_visible() == True