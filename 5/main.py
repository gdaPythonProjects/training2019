from menu import Menu

if __name__ == "__main__":
    menu_manager = Menu()
    menu_manager.print_menu()
    menu_manager.get_menu_option()
    if menu_manager.currentOption == 2:
        print("Coś")
