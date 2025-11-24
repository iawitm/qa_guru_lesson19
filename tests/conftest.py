import dotenv
import pytest
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from selene import browser
import os

dotenv.load_dotenv()
user_name = os.getenv('BROWSERSTACK_USERNAME')
access_key = os.getenv('BROWSERSTACK_ACCESS_KEY')


@pytest.fixture(scope='function', params=['android', 'ios'])
def mobile_setup(request):
    if request.param == 'android':
        options = UiAutomator2Options().load_capabilities({
            # Specify device and os_version for testing
            "platformName": 'android',
            "platformVersion": "11.0",
            "deviceName": "Google Pixel 5",

            # Set URL of the application under test
            "app": "bs://sample.app",

            # Set other BrowserStack capabilities
            'bstack:options': {
                "projectName": "Android tests",
                "buildName": "browserstack-build-1",

                # Set your access credentials
                "userName": user_name,
                "accessKey": access_key
            }
        }
        )

    if request.param == 'ios':
        options = XCUITestOptions().load_capabilities({
            # Specify device and os_version for testing
            "platformName": "ios",
            "platformVersion": "16",
            "deviceName": "iPhone 14",

            # Set URL of the application under test
            "app": "bs://sample.app",

            # Set other BrowserStack capabilities
            'bstack:options': {
                "projectName": "IOS tests",
                "buildName": "browserstack-build-1",

                # Set your access credentials
                "userName": user_name,
                "accessKey": access_key
            }
        }
        )
    browser.config.driver_remote_url = 'http://hub.browserstack.com/wd/hub'
    browser.config.driver_options = options

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    browser.quit()


ios = pytest.mark.parametrize('mobile_setup', ['ios'], indirect=True)
android = pytest.mark.parametrize('mobile_setup', ['android'], indirect=True)
