
while True:
    user = input(
        "indica nombre,edad,direccion y telefono en ese orden usando el formato: usuario[título de lo indicado] = "
        "lo indicado\n")usuario = {}
    if 'terminar' in user:
        print(usuario['nombre'], "tiene", usuario['edad'], "años", "vive en", usuario['direccion'],
              "y su número de teléfono es", usuario['telefono'])
        break
    else:
        print("continúa escribiendo")
