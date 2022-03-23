from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.pages.driver_wrapper import DriverWrapper
from utils.pages.auth_page import AuthWrapper
from utils.pages.main_page import MainWrapper
from utils.helper import load_config

class Application:
    def __init__(self):
        chrome_options = Options()
        # chrome_options.add_argument('--ignore-certificate-errors-spki-list')
        # chrome_options.add_argument('--ignore-certificate-errors')
        # chrome_options.add_argument('--ignore-urlfetcher-cert-requests')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.set_window_size(1920, 1080)
        self.configs = load_config('scores.json')
        self.wrapper = DriverWrapper(self.driver)
        self.auth = AuthWrapper(self)
        self.main = MainWrapper(self.wrapper)