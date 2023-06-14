#!/usr/bin/python3
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

wait = WebDriverWait(driver, 2)
driver.get("https://google.com/ncr")

# driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)
# driver.find_element(By.CSS_SELECTOR, "[name = q]").send_keys("cheese" + Keys.RETURN)
driver.find_element(By.XPATH, "//*[@name = 'q']").send_keys("cheese" + Keys.RETURN)
# first_result = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'h3')))
first_result = wait.until(ec.presence_of_element_located((By.XPATH, './/h3')))
first_result.click()

# word = driver.find_element(By.LINK_TEXT, "casein")
# word = driver.find_element(By.CSS_SELECTOR, "[title*=Casein]")
casein = driver.find_element(By.XPATH, "(.//*[@title='Casein'])[1]")

# parmesan = driver.find_element(By.LINK_TEXT, "Parmesan")
parmesan = driver.find_element(By.XPATH, ".//*[@title='Parmesan']")

brie = driver.find_element(By.LINK_TEXT, "Brie")
# brie = driver.find_element(By.XPATH, ".//*[@title='Brie']")

print(parmesan.text)
print(brie.text)
brie.click()
time.sleep(1)
driver.close()