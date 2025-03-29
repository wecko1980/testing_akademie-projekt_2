import pytest
from playwright.sync_api import sync_playwright

# vytvořím si instanci browser
@pytest.fixture()
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=2000)
        yield browser
        browser.close()

# vytvořím si page v nadefinovaném browseru
@pytest.fixture()
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

def test_invalid_email_newsletter(page):
    page.goto("https://engeto.cz/")
    
    # odkliknu nezbytné cookies
    refuse_button = page.locator("#cookiescript_reject")
    refuse_button.click()

    # najdu button "Termíny" a kliknu na něj a dostanu se na podstránku https://engeto.cz/terminy/
    btn = page.locator("#main-header > div > div > a")
    btn.click()
    
    # ve filtru vlevo najdu prvni checkbox a nastavím jako zaškrtnutý (=použiju filtrování)
    # pozn. musel jsem využít metodu get_by_label, klasický lokátor nefungoval na přesné zacílení jednoho objektu (page.locator("input#technology-python"))
    checkbox_1 = page.get_by_label("Python")
    checkbox_1.check()
    
    # otestuju zda se pod filtrem objevilo tlačítko "Zrušit filtry" (=filtrování je aktivní)
    # musel jsem využít nth() funkci, protože na stránce jsou 2 totožné objekty odpovídají jednomu lokátoru
    btn_filter_cancel = page.locator("a:has-text('Zrušit filtry')").nth(1)
    assert btn_filter_cancel.inner_text() == "Zrušit filtry"