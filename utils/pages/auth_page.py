
from utils.pages.web_elements import TextField, Button
from locators import AuthPageLocators as auth_lctrs

class AuthWrapper:

    def __init__(self, app):
        self.wrap = app.wrapper
        self.app = app

    def open_auth_page(self):
        url = self.app.configs.get('url')
        self.app.driver.get(url)

    def get_username_field(self):
        return TextField(self.wrap, locator=auth_lctrs.fld_username)

    def get_passwd_field(self):
        return TextField(self.wrap, locator=auth_lctrs.fld_password)

    def get_next_button(self):
        return Button(self.wrap, locator=auth_lctrs.btn_switch_to_passwd)

    def get_btn_submit(self):
        return Button(self.wrap, locator=auth_lctrs.btn_submit)

    def switch_to_frame_form(self):
        frame_form = self.wrap.find_element(auth_lctrs.form_iframe)
        self.app.driver.switch_to.frame(frame_form)

    def switch_to_base_frame(self):
        pass

    def login(self):
        username = self.app.configs.get('user').get('username')
        passwd = self.app.configs.get('user').get('password')
        username_fld = self.get_username_field()
        username_fld.insert_text(username)
        next_btn = self.get_next_button()
        next_btn.click()
        passwd_fld = self.get_passwd_field()
        passwd_fld.insert_text(passwd)
        submit_btn = self.get_btn_submit()
        submit_btn.click()



