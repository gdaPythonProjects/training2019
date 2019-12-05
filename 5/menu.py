class Menu:
    def __init__(self):
        print("Hello from class!")
        self.currentOption = 4

    def __del__(self):
        print("Papa!")

    def print_menu(self):
        print("1. Wyjście")
        print("2. Wypisz coś tam")

    def get_menu_option(self):
        self.currentOption = int(input("Podaj opcję z menu: "))
