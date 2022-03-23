from selenium.webdriver.common.by import By

class AuthPageLocators:
    form_iframe = By.XPATH, "//*[@class='ag-popup__frame__layout__iframe']"
    fld_username = By.XPATH, "//*[@name='username']"
    fld_password = By.XPATH, "//*[@name='password']"
    btn_switch_to_passwd = By.XPATH, "//*[@data-test-id='next-button']"
    btn_submit = By.XPATH, "//*[@data-test-id='submit-button']"

class MainPageLocators:
    btn_new_msg = By.XPATH, "//*[@data-title-shortcut='N']"
    fld_addresser_to = By.XPATH, "//*[@data-name='to']//*[@type='text']"
    fld_msg_theme = By.XPATH, "//*[@name='Subject' and @type='text']"
    fld_msg_body = By.XPATH, "//*[@role='textbox']/div[./br]"
    btn_send_msg = By.XPATH, "//*[@data-title-shortcut='Cmd+Enter']"
    btn_close_form_after_send = By.XPATH, "//*[@title='Закрыть']"
