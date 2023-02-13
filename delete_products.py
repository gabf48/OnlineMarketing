import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from csv import DictReader
driver = webdriver.Chrome('./chromedriver')


def open_chrome():




    driver.maximize_window()
    driver.get("https://bigapp.ro/wp-admin/edit.php?post_type=product")
    time.sleep(2)
    driver.find_element(By.ID, 'user_login').send_keys("administrator93")
    driver.find_element(By.ID, 'user_pass').send_keys("g!l(cz3YgZ3FDj6tgoMauoVY")
    driver.find_element(By.ID, "wp-submit").click()

for num in range(0, 333):
    with open('D:\python\gab.csv', 'r') as read_obj:
        # pass the file object to DictReader() to get the DictReader object
        csv_dict_reader = DictReader(read_obj)
        # iterate over each line as a ordered dictionary
        for row in csv_dict_reader:
            # row variable is a dictionary that represents a row in csv
            print(row)
    driver.find_element(By.ID, 'post-search-input').send_keys(row[0])
    driver.find_element(By.ID, 'search-submit').click()

    time.sleep(10)

    results_list = driver.find_elements(By.CSS_SELECTOR, "#the-list tr")
    print(len(results_list))

    if 'Nu am găsit niciun produs' in driver.page_source: print("no found")

if __name__ == '__main__':
    open_chrome()
