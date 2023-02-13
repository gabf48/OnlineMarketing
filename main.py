import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome('./chromedriver')


def open_chrome():
    driver.maximize_window()
    driver.get("https://newdesign.lcm-client.com/demo/home")
    time.sleep(2)
    # driver.find_element(By.ID, "user.name").send_keys("AMSYS Admin")
    # driver.find_element(By.ID, "user.password").send_keys("tZ8Q22d6,$")
    driver.find_element(By.CSS_SELECTOR, '[id="user.name"] input').send_keys("AMSYS Admin")
    driver.find_element(By.CSS_SELECTOR, '[id="user.password"] input').send_keys("tZ8Q22d6,$")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)
    driver.get("https://newdesign.lcm-client.com/demo/matching/1000/2febb78f458be431bfe23a9780f63c06")
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, '[class="searchArea"] input').send_keys('a')
    driver.find_element(By.CSS_SELECTOR, '.fa-search').click()
    time.sleep(10)


    # ActionChains(driver).move_to_element(button).click(button).perform()
    # time.sleep(3)
    # driver.close()


if __name__ == '__main__':
    open_chrome()
