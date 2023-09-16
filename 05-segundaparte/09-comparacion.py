class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
    
    # EQUAL
    # con este metodo le indicamos que debe comparar cuando se esten comparando las intancias
    def __eq__(self, other):
        return self.lat == other.lat and self.lon == other.lon
    
    # NOT EQUAL
    # con este es el contrario, es para comparar las no igualdades 
    # PERO PYTHON SIN NECESIDAD DE ESCRIBIRLO YA INFIERE ESTE METODO ASI QUE NO DEBE ESCRIBIRSE
    def __ne__(self, other):
        return self.lat != other.lat or self.lon != other.lon
    
    # MENOR QUE
    def __lt__(self, other):
        return self.lat + self.lon < other.lat + other.lon
    
    # MENOR O IGUAL
    def __le__(self, other):
        return self.lat + self.lon <= other.lat + other.lon


coords = Coordenadas(45, 27)
coords2 = Coordenadas(45, 27)
coords3 = Coordenadas(44, 27)

print(coords == coords2) #__eq__
print(coords != coords2) #__ne__
print(coords3 < coords2) #__lt__
print(coords3 > coords2) #__lt__
print(coords3 <= coords2) #__le__
print(coords3 >= coords2) #__le__



