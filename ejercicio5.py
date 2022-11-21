# Escribir un programa que cree un diccionario de traducción español-inglés.
# El usuario introducirá las palabras en español e inglés separadas por dos puntos,
# y cada par <palabra>:<traducción> separados por comas, hasta que el usuario introduzca
# la palabra “terminar”. El programa debe crear un diccionario con las palabras
# y sus traducciones. Después pedirá una frase en español y utilizará el diccionario
# para traducirla palabra a palabra. Si una palabra no está en el diccionario debe
# dejarla sin traducir.
traductor = {}
while True:
    spain = str(input("escribe una palabra en español\n"))
    ingles = str(input("escribe su traduccion en ingles\n"))
    traductor[spain] = ingles
    terminar = input('¿quieres terminar?:\n')
    terminar.lower()
    if terminar == "si":
        frase = str(input("escribe una frase\n"))
        for palabra in frase.split():
            if palabra in traductor:
                print(traductor[palabra], end=" ")
        break
    else:
        print("continua")
