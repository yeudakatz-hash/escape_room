from menu.main_menu import main_menu
from flow_manager import *
# from flow_main import *

def main():
    flag = True
    while flag:
        choose = main_menu()
        if choose == "1":
            escape_zone_rooms_management()
        elif choose == "2":
            order_management()
        elif choose == "3":
            reports()
        elif choose == "4":
            flag = False
            print("byyye")
        else:
            continue


main()