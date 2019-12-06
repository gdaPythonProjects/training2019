from managers.menu import Menu
from managers.input import Input
from managers.calculator import Calculator

if __name__ == "__main__":
    menu_manager = Menu()
    input_manager = Input()

    while True:
        menu_manager.print_menu()
        menu_manager.get_menu_option()
        if menu_manager.currentOption == 0:
            break
        elif menu_manager.currentOption == 1:
            input_manager.get_a_value()
        elif menu_manager.currentOption == 2:
            input_manager.get_b_value()
        elif menu_manager.currentOption == 3:
            input_manager.get_a_b_values()
        elif 4 <= menu_manager.currentOption <= 7:
            calc = Calculator()
            if menu_manager.currentOption == 4:
                calc.add_values(input_manager.a, input_manager.b)
            elif menu_manager.currentOption == 5:
                calc.sub_values(input_manager.a, input_manager.b)
            elif menu_manager.currentOption == 6:
                calc.mul_values(input_manager.a, input_manager.b)
            elif menu_manager.currentOption == 7:
                calc.div_values(input_manager.a, input_manager.b)

