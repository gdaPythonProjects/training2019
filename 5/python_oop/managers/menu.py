from managers.input import Input, InputManagerWrongValue


class Menu:
    def __init__(self):
        self.currentOption = -1

    def print_menu(self):
        print("0. Wyjście")
        print("1. Ustaw pole A")
        print("2. Ustaw pole B")
        print("3. Ustaw pole A i B")
        print("4. Dodaj A i B")
        print("5. Odejmij A i B")
        print("6. Pomnóż A i B")
        print("7. Podziel A i B")

    def get_menu_option(self):
        try:
            self.currentOption = int(Input.get_value_stdin("Wybierz opcję z menu: "))
        except InputManagerWrongValue:
            print("Proszę podać wartość liczbową")
