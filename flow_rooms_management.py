from data.rooms import *
from menu.update_menus import update_rooms_menu
from validations.num import *
from validations.name import *



def view_all_rooms():
    print(load_rooms())



def view_full_details_of_a_specific_room():
    name = get_name("Enter name of room: ")
    all_rooms = load_rooms()
    for room in all_rooms:
        if room.get('name').lower() == name:
            return room
    return None



def add_a_new_room():
    name = get_name("enter name to new room: ")
    difficult = get_difficult()
    duration = get_num("enter duration", 100)
    max_player = get_num("enter max people in room: " ,100)
    min_player = get_num("enter min people in room: ", max_player)
    price_per_person = get_num("enter a price to 1 person: ", 200)
    add_room_to_list(name, difficult, duration, max_player, min_player, price_per_person)



# def update_details_of_an_existing_room():
#     choose = str_to_int(update_rooms_menu())
#     if choose == 1:
#         name = get_name("enter new name: ")
#     if choose ==2:
#         pass
#     if choose ==3:
#         pass
#     if choose ==4:
#         pass
#     if choose ==5:
#         pass
#     if choose ==6:
#         pass
#     if choose ==7:
#         pass



def enable_or_disable_a_room():
    name = get_name("Enter name of room: ")
    rooms = load_rooms()
    for room in rooms:
        if room["name"] == name:
            room["is_active"] = not room["is_active"]
            dump_rooms(rooms)
