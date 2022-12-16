import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.arredo.com.ar/")
# LOGIN
time.sleep(5)

driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div/div[2]/div/div/button").click()
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div/div/div/div[2]/div/div/div/div[1]/ul/li[2]/div/button").click()
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div/div/div/div[2]/div/div/div/div/form/div[1]/label/div/input").send_keys("fruxafrauquoppe-8760@yopmail.com")
driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div/div/div/div[2]/div/div/div/div/form/div[2]/div/label/div/input").send_keys("123456789Ma")
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div/div/div/div[2]/div/div/div/div/form/div[4]/div[2]/button").click()
time.sleep(8)
print("-----------------------------------------------------------------------------------------------------------")
# driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div[2]/a[2]").click()