from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from userdetails import *


class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(r'user-data-dir=C:\Users\NOTE\PycharmProjects\ChromeAutomatization\Perfil')
        self.chrome = webdriver.Chrome(options=self.options)

    def clica_login(self):
        try:
            btn_sign_in = WebDriverWait(self.chrome, 10).until(
                ec.presence_of_element_located((By.LINK_TEXT, 'Sign in'))
            )
            btn_sign_in.click()
        except Exception as e:
            print(f"Erro ao clicar em 'Sign in': {str(e)}")

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def clica_perfil(self):
        try:
            perfil = self.chrome.find_element(By.CLASS_NAME, 'AppHeader-user')
            perfil.click()
        except Exception as e:
            print('erro ao clicar no perfil', e)

    def faz_login(self):
        try:
            input_login = self.chrome.find_element(By.ID, 'login_field')
            input_password = self.chrome.find_element(By.ID, 'password')
            btn_login = WebDriverWait(self.chrome, 10).until(
                ec.presence_of_element_located((By.NAME, 'commit'))
            )
            input_login.send_keys('GustavoGuerato')
            input_password.send_keys('gg08142325')
            sleep(14)
            btn_login.click()
        except Exception as e:
            print(f"Erro ao clicar em 'Sign in': {str(e)}")


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://github.com/')
    chrome.clica_login()
    chrome.faz_login()
    chrome.clica_perfil()
    sleep(20)
    chrome.sair()
