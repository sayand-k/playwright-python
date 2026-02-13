import pytest
from playwright.sync_api import sync_playwright
from utils.config import HEADLESS, BROWSER


@pytest.fixture(scope="function")
def page(request):
    with sync_playwright() as p:
        if BROWSER == "chromium":
            browser = p.chromium.launch(headless=HEADLESS)
        elif BROWSER == "firefox":
            browser = p.firefox.launch(headless=HEADLESS)
        else:
            browser = p.webkit.launch(headless=HEADLESS)

        page = browser.new_page()
        yield page
        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            page.screenshot(path=f"screenshots/{item.name}.png")
