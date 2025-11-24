import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

from tests.conftest import android


@allure.title('Проверка клика по статье')
@allure.description('Клик по статье Frog')
@android
def test_click(mobile_setup):
    with allure.step('Нажимаем на строку поиска'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()

    with allure.step('Ищем Frog'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Frog')
        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name='screenshot',
            attachment_type=allure.attachment_type.PNG,
        )

    with allure.step('Проверяем, что первая статья - Frog'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.first.should(have.text('Frog'))
        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name='screenshot',
            attachment_type=allure.attachment_type.PNG,
        )

    with allure.step('Кликаем по первой статье Frog'):
        results.first.click()
