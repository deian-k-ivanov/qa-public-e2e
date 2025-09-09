import pytest
from constants import DEFAULT_BROWSER_NAME
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser_name():
    return DEFAULT_BROWSER_NAME


@pytest.fixture(scope="session")
def playwright_instance():
    # Start Playwright
    with sync_playwright() as playwright:
        # Map get_by_test_id() to "data-test" (SauceDemo uses this attribute)
        playwright.selectors.set_test_id_attribute("data-test")
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance, browser_name):
    if browser_name == "chromium":
        browser = playright_browser = playwright_instance.chromium
    elif browser_name == "firefox":
        playright_browser = playwright_instance.firefox
    elif browser_name == "webkit":
        playright_browser = playwright_instance.webkit
    else:
        raise ValueError(f"Unsupported browser: {browser_name!r}. Use one of: chromium, firefox, webkit.")

    browser = playright_browser.launch(headless=True)
    yield browser
    browser.close()


@pytest.fixture
def browser_context(browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()
