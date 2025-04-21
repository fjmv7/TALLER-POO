

from biblioteca import Publicacion, Libro, Revista

def mostrar_menu():
    print("\n--- Sistema de Biblioteca ---")
    print("1. Agregar nueva publicación")
    print("2. Prestar publicación")
    print("3. Devolver publicación")
    print("4. Mostrar todas las publicaciones")
    print("5. Salir")

def agregar_publicacion(publicaciones: list):
    print("\nTipo de publicación:")
    print("1. Libro")
    print("2. Revista")
    tipo = input("Seleccione (1-2): ")
    
    titulo = input("Título: ")
    autor = input("Autor: ")
    
    if tipo == "1":
        isbn = input("ISBN: ")
        paginas = int(input("Número de páginas: "))
        publicaciones.append(Libro(titulo, autor, isbn, paginas))
    else:
        issn = input("ISSN: ")
        numero = int(input("Número de revista: "))
        publicaciones.append(Revista(titulo, autor, issn, numero))
    
    print("¡Publicación agregada con éxito!")

def main():
    publicaciones = []
    
    # Ejemplos corregidos
    publicaciones.append(Libro("Cien años de soledad", "Gabriel García Márquez", "978-0307474728", 417))
    publicaciones.append(Revista("National Geographic", "Varios autores", "ISSN-0027-9358", 245))
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_publicacion(publicaciones)
        elif opcion == "2":
            titulo = input("Título a prestar: ")
            for pub in publicaciones:
                if pub.titulo.lower() == titulo.lower():
                    print(pub.prestar())
                    break
            else:
                print("Publicación no encontrada")
        elif opcion == "3":
            titulo = input("Título a devolver: ")
            for pub in publicaciones:
                if pub.titulo.lower() == titulo.lower():
                    print(pub.devolver())
                    break
            else:
                print("Publicación no encontrada")
        elif opcion == "4":
            print("\n--- Catálogo completo ---")
            for pub in publicaciones:
                print(pub)
                print("-" * 40)
        elif opcion == "5":
            print("Saliendo del sistema..." \
            "Que tenga lindo dia")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()