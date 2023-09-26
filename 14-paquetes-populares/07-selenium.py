from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

options = webdriver.ChromeOptions() # opciones por defecto, poderlas manipular
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)
browser.implicitly_wait(10) # el explorador debe esperar antes de determinar que no encontro nada, en este caso 10 seg
browser.get("https://github.com") # indicamos que sitio quiere que visite

# el ejercicio consistira en apretar el boton de login y que el ingrese los datos de login y pinche el boton entrar y valide si mi nombre esta dentro de una seccion en particular
link = browser.find_element(By.LINK_TEXT, "Sign in") # aqui se pueden utilizar clasess id, etc, en esta ocasion uso el texto gia
link.click()

# ahora rellenamos el formulario
user_input = browser.find_element(By.ID, "login_field")
pass_input = browser.find_element(By.ID, "password")

user_input.send_keys("santiscano@gmail.com")
pass_input.send_keys(os.environ.get("gh_pass"))

# ahora sigue el enter de la tecla
pass_input.send_keys(Keys.RETURN)

# ahora validemos si mi nombre de usuario esta en la web
profile = browser.find_element(By.CLASS_NAME, "css-truncate.css-truncate-target.ml1")
label = profile.get_attribute("innerHTML")
print(label)

# INDICAR A SELENIUM DE QUE FALTE ALGO

assert "Santiscano" in label

# cerrar el explorador al finalizar los test
browser.quit()




