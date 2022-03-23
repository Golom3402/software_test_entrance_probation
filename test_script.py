from utils.app import Application
import pytest

@pytest.fixture()
def app():
    app = Application()
    yield app
    app.driver.quit()

def test_to_send_msg(app):
    app.auth.open_auth_page()
    app.auth.switch_to_frame_form()
    app.auth.login()
    address = "golom3402@gmail.com"
    subject = "test"
    msg_text = "Тестовое задание, просьба удалить данное сообщение."
    app.main.send_new_message(to=address, subject=subject, msg_text=msg_text)

