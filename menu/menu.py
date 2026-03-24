import questionary


def mostrar_menu_principal():
    return questionary.select(
        "selecciona una opcion:",
        choices=[
            "ver menu",
            "buscar plato",
            "agregar al pedido",
            "ver pedido",
            "salir"
        ],
    ).ask()


def pedir_texto(mensaje:str):
    return questionary.text(mensaje).ask()

def pedir_numero(mensaje:str):
    valor = questionary.text(mensaje).ask()
    return int(valor)


mostrar_menu_principal()
