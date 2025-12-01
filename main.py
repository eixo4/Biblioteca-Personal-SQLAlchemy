import os
from database import GestorBiblioteca


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_tabla(libros):
    if not libros:
        print("\n(No se encontraron libros)")
        return

    print("\n" + "=" * 95)
    print(f"{'ID':<5} | {'TÍTULO':<30} | {'AUTOR':<25} | {'GÉNERO':<15} | {'ESTADO':<10}")
    print("-" * 95)

    for libro in libros:
        print(f"{libro.id:<5} | {libro.titulo:<30} | {libro.autor:<25} | {libro.genero:<15} | {libro.estado:<10}")
    print("=" * 95 + "\n")


def menu_principal():
    gestor = GestorBiblioteca()

    while True:
        print("\n--- 🐬 GESTOR DE BIBLIOTECA (MariaDB + SQLAlchemy) ---")
        print("1. Agregar nuevo libro")
        print("2. Ver todos los libros")
        print("3. Buscar libro")
        print("4. Actualizar libro")
        print("5. Eliminar libro")
        print("6. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == '1':
            print("\n--- Agregar Libro ---")
            titulo = input("Título: ")
            autor = input("Autor: ")
            genero = input("Género: ")
            estado = "Leído" if input("¿Leído? (s/n): ").lower() == 's' else "No leído"

            if gestor.agregar_libro(titulo, autor, genero, estado):
                print("✅ ¡Libro guardado en MariaDB!")

        elif opcion == '2':
            libros = gestor.listar_libros()
            mostrar_tabla(libros)

        elif opcion == '3':
            termino = input("\nIngrese término de búsqueda: ")
            resultados = gestor.buscar_libros(termino)
            mostrar_tabla(resultados)

        elif opcion == '4':
            print("\n--- Actualizar Libro ---")
            mostrar_tabla(gestor.listar_libros())
            try:
                id_libro = int(input("ID del libro a modificar: "))
                print("(Deje vacío para mantener el valor actual)")

                # Recolectamos datos
                t = input("Nuevo título: ")
                a = input("Nuevo autor: ")
                g = input("Nuevo género: ")
                e_in = input("Nuevo estado (s/n): ").lower()

                # Preparamos diccionario de cambios
                cambios = {}
                if t: cambios['titulo'] = t
                if a: cambios['autor'] = a
                if g: cambios['genero'] = g
                if e_in == 's':
                    cambios['estado'] = 'Leído'
                elif e_in == 'n':
                    cambios['estado'] = 'No leído'

                if gestor.actualizar_libro(id_libro, **cambios):
                    print("✅ Actualización exitosa.")
                else:
                    print("❌ No se encontró el ID o hubo un error.")

            except ValueError:
                print("❌ ID inválido.")

        elif opcion == '5':
            print("\n--- Eliminar Libro ---")
            mostrar_tabla(gestor.listar_libros())
            try:
                id_libro = int(input("ID a eliminar: "))
                if input("¿Confirmar? (s/n): ").lower() == 's':
                    if gestor.eliminar_libro(id_libro):
                        print("✅ Libro eliminado.")
                    else:
                        print("❌ Error o ID no encontrado.")
            except ValueError:
                print("❌ ID inválido.")

        elif opcion == '6':
            print("¡Hasta luego!")
            break


if __name__ == "__main__":
    menu_principal()