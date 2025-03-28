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

    # najdu input pro vložení e-mailové adresy pro odběr newsletteru a vložím ji v nevalidním tvaru (použiju # místo @)
    text_input = page.locator("input[type='email']")
    text_input.fill("test#test.cz")
    
    # najdu button pro odeslání přihlášení k odběru newsletteru
    button = page.locator("a:has-text('Odebírat')")
    button.click()
    
    # otestuju zda se pod polem pro zadání e-mailové adresy zobrazí příslušná chybová hláška
    span = page.locator("span:has-text('Prosím zadejte validní emailovou adresu')")
    assert span.inner_text() == "Prosím zadejte validní emailovou adresu"