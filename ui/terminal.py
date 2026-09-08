from modelos.pelicula import Pelicula
import json


def cargar_datos():
    with open("datos/peliculas.json", "r", encoding="utf-8") as f:
        datos = json.load(f)
    peliculas = []
    for d in datos:
        peliculas.append(Pelicula(d["titulo"], d["genero"], d["rating"], d["anio"]))
    return peliculas


def mostrar_menu():
    print("=" * 40)
    print(" SISTEMA DE RECOMENDACIONES")
    print("=" * 40)
    print("1. Buscar elemento")
    print("2. Listar elementos")
    print("3. Filtrar por genero")
    print("0. Salir")
    print("-" * 40)


def buscar(peliculas):
    titulo = input("Titulo a buscar: ")
    for p in peliculas:
        if titulo.lower() in p.titulo.lower():
            print(p)
    print("Fin de resultados.")


def listar(peliculas):
    for i, p in enumerate(peliculas, 1):
        print(f"{i}. {p}")


def filtrar(peliculas):
    genero = input("Genero a filtrar: ")
    for p in peliculas:
        if genero.lower() in p.genero.lower():
            print(p)


def main():
    peliculas = cargar_datos()
    while True:
        mostrar_menu()
        opcion = input("Opcion: ")
        if opcion == "1":
            buscar(peliculas)
        elif opcion == "2":
            listar(peliculas)
        elif opcion == "3":
            filtrar(peliculas)
        elif opcion == "0":
            print("Hasta luego!")
            break


if __name__ == "__main__":
    main()