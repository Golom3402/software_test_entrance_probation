from selenium.webdriver import Keys


class TextField:
    """
    Класс описывающий поведение  и взаимодействие с типовым текстовым полем

    """
    def __init__(self, wrapper, locator):
        self.wrap = wrapper
        self.web_element = self.wrap.wait_to_visible(locator)
        self.locator = locator

    def click(self, wait=True):
        if wait:
            self.wrap.wait_to_clickable(self.locator)
        self.web_element.click()

    def insert_text(self, text, clear=True):
        """
        метод кликает на текстовое поле,  и вводит в него текст из параметра  text
        :param text: str, текст, который будет вставлен в текстовое поле
        :param clear: bool, Если True - то поле будет принудительно очищено
        :return:
        """
        self.web_element = self.wrap.find_element(self.locator)
        self.wrap.click(self.locator)
        if clear:
            self.clear_text_field()
        self.web_element.send_keys(text)

    def clear_text_field(self):
        """
        Метод очищает текстовое поле, если оно не очистилось штатным методом селениума clear - то выполняется клик,
        и ввод комбинаций клавиш на выделение и удаление текста
        """
        self.web_element.clear()
        if self.get_current_values():
            self.wrap.click(self.locator)
            self.web_element.send_keys(Keys.CONTROL + "a")
            self.web_element.send_keys(Keys.DELETE)
        if self.get_current_values():
            self.web_element.send_keys(Keys.HOME)
            self.web_element.send_keys(Keys.SHIFT, Keys.END)
            self.web_element.send_keys(Keys.DELETE)

    def get_current_values(self, any_text_inside=False):
        """
        Метод возвращает значение из атрибута value в строке ввода
        """
        return self.web_element.get_attribute('value') or self.web_element.text

class Button:
    """
    Класс описывает поведение и методы для взаимодействия с типовым объектом кнопки,
    """
    def __init__(self, wrapper, locator):
        self.wrap = wrapper
        self.locator = locator
        self.web_element = self.wrap.wait_to_visible(locator)

    def click(self):
        """
        Клик по кнопке
        """
        self.wrap.click(locator=self.locator)

