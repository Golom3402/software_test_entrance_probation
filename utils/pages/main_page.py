from locators import MainPageLocators as main_lctrs
from utils.pages.web_elements import TextField, Button


class MainWrapper:
    """
    Класс представляющий главную страницу веб-клиента mail.ru, и содержащий методы для взаимодействия с некоторыми
    элементами страницы
    """

    def __init__(self, wrapper):
        self.wrap = wrapper

    def get_btn_new_msg(self):
        return Button(self.wrap, main_lctrs.btn_new_msg)

    def get_btn_send_msg(self):
        return Button(self.wrap, main_lctrs.btn_send_msg)

    def get_fld_subject(self):
        return TextField(self.wrap, main_lctrs.fld_msg_theme)

    def get_fld_addressee(self):
        return TextField(self.wrap, main_lctrs.fld_addresser_to)

    def get_fld_msg_body(self):
        return TextField(self.wrap, main_lctrs.fld_msg_body)

    def get_btn_close_form_after_send(self):
        return Button(self.wrap, main_lctrs.btn_close_form_after_send)

    def send_new_message(self, to: str, msg_text, subject=None):
        """
        Метод находит кнопку "Написать письмо", кликает по ней,
        находит ключевые поля для создания нового сообщения, и заполняет их,
        кликает на кнопку "Отправить"
        Закрывает всплывающую форму с отменой отправки сообщения
        :param to: адрес электронной почты получателя
        :param msg_text: текст сообщения
        :param subject: тема сообщения
        :return:
        """
        new_msg_btn = self.get_btn_new_msg()
        new_msg_btn.click()
        address_fld = self.get_fld_addressee()
        address_fld.insert_text(to)
        if subject and isinstance(subject, str):
            subject_fld = self.get_fld_subject()
            subject_fld.insert_text(subject)
        body_msg_fld = self.get_fld_msg_body()
        body_msg_fld.insert_text(msg_text)
        send_btn = self.get_btn_send_msg()
        send_btn.click()
        close_form_btn = self.get_btn_close_form_after_send()
        close_form_btn.click()




