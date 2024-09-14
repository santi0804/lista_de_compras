# validador.py

def validar_contraseña(contraseña):

    if len(contraseña) < 8:
        return False

    contiene_mayuscula = False
    contiene_minuscula = False
    contiene_numero = False
    contiene_especial = False
    caracteres_especiales = "!@#$%^&*"

    for char in contraseña:
        if char.isupper():
            contiene_mayuscula = True
        elif char.islower():
            contiene_minuscula = True
        elif char.isdigit():
            contiene_numero = True
        elif char in caracteres_especiales:
            contiene_especial = True

    return contiene_mayuscula and contiene_minuscula and contiene_numero and contiene_especial

# Solicitar contraseña al usuario
def main():
    contraseña = input("Introduce una contraseña para validar: ")
    if validar_contraseña(contraseña):
        print("La contraseña es válida.")
    else:
        print("La contraseña no cumple con los criterios.")

if __name__ == "__main__":
    main()
