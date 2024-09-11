
lista_compras = []  # Inicia lista vacia

while True:
    print("\nMenú principal:")
    print("1. Agregar artículo")
    print("2. Mostrar Lista")
    print("3. Eliminar artículo")
    print("4. Salir")

    opcion = input("Selecciona una opción (1-4): ")

    if opcion == '1':   # Agregar artículo
            articulo = input("Nombre del articulo: ") 
            lista_compras.append(articulo)
            print(f"'{articulo}' agregado a la lista.")

    elif opcion == '2':  

        if lista_compras:    #Eliminar articulo
            print("\nLista actual: ")
            for i, item in enumerate(lista_compras):
                print(f"{i + 1}. {item}")
            
            try:
                indice = int(input("Ingrese número del articulo a eliminar: ")) -1
                if 0 <= indice < len(lista_compras):
                     eliminado = lista_compras.pop(indice)
                     print(f"\ '{eliminado}' ha sido eliminado.")
                else:
                    print("indice invalido.")
            except ValueError:
                 print("Ingrese numero válido.")

        else:
            print("la lista esta vacía.")

    elif opcion == '3':      # Mostrar lista
        if lista_compras:
              print(f"\nLista de compras: ")
              for i, item in enumerate(lista_compras):
                   print(f"{i + 1}. {item}")
        else:
             print("Lista vacia.")


    elif opcion == '4':  #Salir del programa
         print("!Gracias por utilizar la lista de comprar! vuelve pronto putito.")
         break

    else:
         print("Opción no valida, elige una opción entre 1 y 4.")

         





