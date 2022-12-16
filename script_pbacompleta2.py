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
# Primer script y validación label del botón "AGREGAR".
driver.find_element(By.XPATH, '//*[@id="downshift-0-input"]').send_keys("juego de sábanas 1 plaza")
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div/div[1]/div/div/div[1]/div/label/div/span/div/div/button").click()
time.sleep(15)

driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div/div/section/div[2]/div/div[4]/div/div[2]/div/div[2]/div[2]/div[1]/section/a/article/div[2]/div[1]/div/div/img[1]").click()
time.sleep(15)

driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[1]/div[2]/section/div/div[2]/div/div[4]/div/div/div/div").click()
driver.find_element(By.XPATH, "/html/body/div[8]/div[1]/div/button").click()

driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[1]/div[2]/section/div/div[2]/div/div[5]/div/div/div[1]/div/div/div/div/div/div/div[1]/button").click()
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[1]/div[2]/section/div/div[2]/div/div[5]/div/div/div[1]/div/div/div/div/div/div/div[1]/button").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[1]/div[2]/section/div/div[2]/div/div[5]/div/div/div[2]/div/div/button").click()
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div/div[3]/aside/div/div/button").click()
time.sleep(8)
driver.find_element(By.XPATH, "/html/body/div[6]/div/div[1]/button").click()
time.sleep(5)

# Validación label boton "AGREGAR"
print("----------------------------------------------------------------------------------------")
botonAgregar = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[1]/div[2]/section/div/div[2]/div/div[5]/div/div/div[2]/div/div/button")
labelBotonAgregar = botonAgregar.text

labelRequerido = "AGREGAR"

print(f"El label requerido del botón: {labelRequerido}")

def check_label(s):
    if re.match(labelRequerido, s):
        print("Pass")
    else:
        print("Fail")
check_label(labelBotonAgregar)
print(f"El label que tiene el botón es: {labelBotonAgregar}")
print("---------------------------------------------------------------------------------------------")
# Segundo script y validación del label del botón "VACIAR CARRITO"
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="downshift-0-input"]').send_keys("bata de baño infantil con capucha")
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div/div[1]/div/div/div[1]/div/label/div/span/div/div/button").click()
time.sleep(15)
# driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div[2]/a[2]").click()
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div/div/section/div[2]/div/div[4]/div/div[2]/div/div[2]/div[2]/div/section/a/article/div[2]/div[1]/div/div/img[1]").click()
time.sleep(15)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[1]/div[2]/section/div/div[2]/div/div[5]/div/div/div[1]/div/div/div/div/div/div/div[1]/button").click()
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[1]/div[2]/section/div/div[2]/div/div[5]/div/div/div[1]/div/div/div/div/div/div/div[1]/button").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[1]/div[2]/section/div/div[2]/div/div[5]/div/div/div[2]/div/div/button").click()
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div/div[3]/aside/div/div/button").click()
time.sleep(7)

# Validación label boton "VACIAR CARRITO".
botonVaciarCarrito = driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/div/div/div[3]/div/div/button")
labelVaciarCarrito = botonVaciarCarrito.text

labelRequerido = "VACIAR CARRITO"

print(f"El label requerido del botón es: {labelRequerido}")

check_label(labelVaciarCarrito)
print(f"El label que tiene el botón es: {labelVaciarCarrito}")
print("------------------------------------------------------------------------------------------")

driver.find_element(By.XPATH, "/html/body/div[6]/div/div[1]/button").click()
