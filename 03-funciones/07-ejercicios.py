def not_space(text):
    new_text = ""

    for char in text:
        if char != " ":
            new_text += char
    
    return new_text

def reverse(text):
    text_reverse = ""
    for char in text:
        text_reverse = char + text_reverse
    
    return text_reverse

def es_palindromo(text):
    notSpace = not_space(text)
    textReverse = reverse(notSpace)
    return notSpace.lower() == textReverse.lower()

print("Abba", es_palindromo("Abba"))
print("Reconocer", es_palindromo("Reconocer"))
print("Amo la paloma", es_palindromo("Amo la paloma"))
print("Hola mundo", es_palindromo("Hola mundo"))