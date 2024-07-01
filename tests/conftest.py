import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def browser_setting():
    browser.config.base_url = "https://guru.qahacking.ru"
    browser.config.window_height = 1800
    browser.config.window_width = 1200

    yield browser

    # attach.add_html(browser)
   # attach.add_screenshot(browser)
   # attach.add_logs(browser)
  #  attach.add_video(browser)

    browser.quit()
