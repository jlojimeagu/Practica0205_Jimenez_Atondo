alumnado = {}
while True:
    print('***********************************************')
    print('*                                             *')
    print('*          ¿que deseas hacer?                 *')
    print('*         (1) Añadir alumno/a                 *')
    print('*         (2) Eliminar alumno/a               *')
    print('*         (3) Mostrar alumno/a                *')
    print('*         (4) Listar todo el alumnado         *')
    print('*         (5) Listar alumnado aprobado        *')
    print('*         (6) Terminar                        *')
    print('*                                             *')
    print('***********************************************')
    pregunta = int(input())
    if pregunta == 1:
        nif = input('Introduce NIF del alumno:\n')
        nombre = input('Introduce el nombre del alumno:\n')
        direccion = input('Introduce la dirección del alumno:\n')
        telefono = input('Introduce el teléfono del alumno:\n')
        email = input('Introduce el correo electrónico del alumno:\n')
        nota = input('¿aprobo el alumno (si/no)?\n')
        datos = {'nombre': nombre, 'dirección':direccion, 'teléfono':telefono, 'email':email, 'preferente':nota}
        alumnado[nif] = datos
    
    if pregunta == 2:

    if pregunta == 3:

    if pregunta == 4:

    if pregunta == 5:

    if pregunta == 6:

    else:
        print('lo introducido es erroneo')