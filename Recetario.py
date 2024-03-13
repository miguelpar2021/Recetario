import os
from pathlib import Path
from os import system

mi_ruta=Path(Path.home(), "Recetas")

def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador +=1

    return contador

def inicio():
    system('cls')
    print('-'*30)
    print("Bienvenidos a tu Recetario")
    print('-' * 30)
    print(f'Las recetas estan en {mi_ruta}')
    print(f"Total de Recetas: {contar_recetas(mi_ruta)}\n")

    eleccion_menu= 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print("-------------Menu Pricipal----------------")
        print('\n')
        print('Leer Recete[1]')
        print('Crea Receta[2]')
        print('Crea Categoria[3]')
        print('Eliminar Receta[4]')
        print('Eliminar Categoria[5]')
        print('Finizalizar Codigo[6]\n')
        eleccion_menu =input()
    return int(eleccion_menu)


def mostrar_categorias(ruta):
    print("Categorias")
    ruta_categorias=Path(ruta)
    lista_categorias=[]
    contador = 1

    for carpeta in ruta_categorias.iterdir():
        carpeta_str= str(carpeta.name)
        print(f'{contador} - {carpeta_str}')
        lista_categorias.append(carpeta)
        contador += 1
    return lista_categorias

def elegir_categoria(lista):
    eleccion_correcta='x'

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1 , len(lista) +1):
        eleccion_correcta=input('\nElije una categoria:')
    return lista[int(eleccion_correcta) -1]

def mostrar_recetas(ruta):
    print("Estas son las recetas")
    ruta_recetas=Path(ruta)
    lista_recetas=[]
    contador_recetas= 1

    for receta in ruta_recetas.glob('*.txt'):
        receta_str=str(receta.name)
        print(f'{contador_recetas} - {receta_str}')
        lista_recetas.append(receta)
        contador_recetas +=1
    return lista_recetas

def elegir_receta(lista):
    eleccion_receta='x'

    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1 , len(lista) +1):
       eleccion_receta=input('\nElije una receta:')

    return lista[int(eleccion_receta) -1]


def leer_receta_(receta):
    print(Path.read_text(receta))

def crear_receta(ruta):
    existe= False

    while not existe:
        print("Escribe el Nombre de tu receta")
        nombre_receta=input() + '.txt'
        print("Escribe tu nueva receta")
        contenido_receta=input()
        ruta_nueva=Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva,contenido_receta)
            print(f"Tu receta {nombre_receta} a sido creada ")
            existe=True
        else:
            print("Lo siento, esta receta ya existe")

def crear_categoria(ruta):
    existe= False

    while not existe:
        print("Escribe el Nombre de tu nueva Categoria")
        nombre_categoria=input()
        ruta_nueva=Path(ruta,nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu categoria {nombre_categoria} a sido creada ")
            existe=True
        else:
            print("Lo siento, esta receta ya existe")

def eliminar_receta(receta):
    Path(receta).unlink()
    print(f'La receta {receta.name} ha sido eliminada')

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f'La receta {categoria.name} ha sido eliminada')

def volver_inicio():
    eleccio_regresar='x'

    while eleccio_regresar.lower() != 'v':
        eleccio_regresar=input('\nPresione V para regresar al Menu: ')


finalizar_programa=False

while not finalizar_programa:
    eleccion=inicio()
    if eleccion==1:
            mis_categorias = mostrar_categorias(mi_ruta)
            mi_categoria=elegir_categoria(mis_categorias)
            mis_recetas=mostrar_recetas(mi_categoria)
            if len(mis_recetas) < 1:
                print("no hay recetas en esta categoría.")
            else:
                mi_receta = elegir_receta(mis_recetas)
                leer_receta_(mi_receta)
                volver_inicio()


    elif eleccion==2:
            mis_categorias=mostrar_categorias(mi_ruta)
            mi_categoria = elegir_categoria(mis_categorias)
            crear_receta(mi_categoria)
            volver_inicio()

    elif eleccion==3:
            crear_categoria(mi_ruta)
            volver_inicio()

    elif eleccion==4:
            mis_categorias=mostrar_categorias(mi_ruta)
            mi_categoria = elegir_categoria(mis_categorias)
            mis_recetas=mostrar_recetas(mi_categoria)
            mi_receta=elegir_receta(mis_recetas)
            eliminar_receta(mi_receta)
            volver_inicio()

    elif eleccion==5:
            mis_categorias=mostrar_categorias(mi_ruta)
            mi_categoria = elegir_categoria(mis_categorias)
            eliminar_categoria(mi_categoria)
            volver_inicio()

    elif eleccion==6:
            print("Muchas gracias adios")
            finalizar_programa=True
            #Finalizar Programa"""


