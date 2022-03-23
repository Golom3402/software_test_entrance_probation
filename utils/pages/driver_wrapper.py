from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class DriverWrapper:

    def __init__(self, driver):
        self.driver = driver

    # Поиск элемента
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    # Клик по элементу
    def click(self, locator):
        self.wait_to_clickable(locator).click()

    def wait_to_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator),
                                             message=f'Не дождались отображения элемента {locator}')

    def wait_to_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(locator),
                                             message=f'Не дождались кликабельности элемента {locator}')



