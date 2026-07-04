from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import URL_LOGIN, USUARIO, SENHA


def realizar_login(driver):

    driver.get(URL_LOGIN)

    WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.NAME,"usuario"))
    )

    driver.find_element(By.NAME,"usuario").send_keys(USUARIO)

    driver.find_element(By.NAME,"senha").send_keys(SENHA)

    driver.find_element(By.TAG_NAME,"button").click()