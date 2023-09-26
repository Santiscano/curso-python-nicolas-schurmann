import requests
from bs4 import BeautifulSoup as soup # no es para navegar al sitio web sino que recibe un string

url = "https://stackoverflow.com/questions"
respuesta = requests.get(url)
texto = respuesta.text

# se entrega el texto y se indica el interprete de lo que se le esta pasando
bSoup = soup(texto, "html.parser")
preguntas = bSoup.select(".s-post-summary") # selecciona todos los elementos que tengan esa clase html

# acceder  cualquier atributo html
# print(preguntas[0]["href"]) # aqui accedi al href y asi podria hacerlo con cualquier atributo

for pregunta in preguntas:
    titulo = pregunta.select_one(".s-link").get_text() # selecciono 1 elemento y con get_text veo le texto de este
    usuario = pregunta.select_one(".s-user-card--link").get_text() # busca usuario
    print(f"{usuario.strip()} - Titulo: \n{titulo.strip()}") # strip() elimina espacios






