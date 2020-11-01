from draw_menu import draw_menu
from const_variables import main_menu
def main():
    #print("-"*80,"main OK")

    while True:

        menu_option = draw_menu(main_menu,'baaaabca')
                
        if menu_option == 3:
            input("Exit")
            return




if __name__ == "__main__":
    main()
