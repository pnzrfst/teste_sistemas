from selenium import webdriver
from selenium.webdriver.common.by import By
import time

navegador = webdriver.Chrome()
navegador.maximize_window()

navegador.get("https://www.facebook.com/")

email_input = navegador.find_element(By.NAME , "email").send_keys("jose-brunoj@hotmail.com")
password_input = navegador.find_element(By.NAME, "pass").send_keys("124125412")

botao_verde = navegador.find_element(by="class name", value="_42ft, _4jy0, _6lti, _4jy6, _4jy2_ selected _51sy")
botao_verde.click()
time.sleep(2)



time.sleep(2)
time.sleep(120)