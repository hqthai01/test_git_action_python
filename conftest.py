import os
import sys
import time
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

test_path = os.path.dirname(__file__)
test_report_path = test_path + '/reports'
sys.path.append(test_path)
sys.path.append(test_report_path)
chrome_path = test_path + '/chromedriver'

@pytest.fixture(autouse=True)
def chrome_driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--window-size=1920,1080")
    global driver
    driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_path)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()
    print('Test completed')

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    timestamp = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' and report.outcome == 'failed':
        path = test_report_path + '/' + str(item).removeprefix('<Function ').removesuffix('>') + '_' +timestamp+'.png'
        time.sleep(3)
        driver.save_screenshot(path)
        extra.append(pytest_html.extras.image(path))
        extra.append(pytest_html.extras.url(driver.current_url))
        report.extra = extra