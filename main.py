from biblioteca import Publicacion, Libro, Revista

def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n--- Sistema de Biblioteca ---")
    print("1. Agregar nueva publicación")
    print("2. Prestar publicación")
    print("3. Devolver publicación")
    print("4. Mostrar todas las publicaciones")
    print("5. Salir")

def agregar_publicacion(publicaciones: list):
    """Agrega una nueva publicación al sistema"""
    print("\nTipo de publicación:")
    print("1. Libro")
    print("2. Revista")
    tipo = input("Seleccione (1-2): ")
    
    titulo = input("Título: ")
    autor = input("Autor: ")
    año = int(input("Año de publicación: "))
    
    if tipo == "1":
        isbn = input("ISBN: ")
        paginas = int(input("Número de páginas: "))
        publicaciones.append(Libro(titulo, autor, año, paginas, isbn))  # CORREGIDO: orden de parámetros
    else:
        issn = input("ISSN: ")
        numero = int(input("Número de revista: "))
        publicaciones.append(Revista(titulo, autor, año, numero, issn))  # CORREGIDO: orden de parámetros
    
    print("¡Publicación agregada con éxito!")

def main():
    """Función principal del programa"""
    publicaciones = []
    
    # Ejemplos de publicaciones para pruebas - CORREGIDOS los parámetros
    publicaciones.append(Libro("Cien años de soledad", "Gabriel García Márquez", 1967, 417, "978-0307474728"))
    publicaciones.append(Revista("National Geographic", "Varios autores", 2023, 245, "ISSN-0027-9358"))
    
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
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()