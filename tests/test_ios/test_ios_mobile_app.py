import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

from tests.conftest import ios


@allure.title('Проверка клика в меню')
@allure.description('Клик по Web View')
@ios
def test_ios_click(mobile_setup):
    with allure.step("Проверка названия второго элемента в меню (Web View)"):
        browser.element((AppiumBy.XPATH, "//XCUIElementTypeTabBar//XCUIElementTypeButton[2]")).should(
            have.text('Web View'))
        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name='screenshot',
            attachment_type=allure.attachment_type.PNG,
        )

    with allure.step("Клик по Web View"):
        browser.element((AppiumBy.XPATH, "//XCUIElementTypeTabBar//XCUIElementTypeButton[2]")).click()
        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name='screenshot',
            attachment_type=allure.attachment_type.PNG,
        )
