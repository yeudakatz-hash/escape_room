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
    print("The room not exist")



def add_a_new_room():
    name = get_name("enter name to new room: ")
    difficult = get_difficult()
    duration = get_num("enter duration", 100)
    max_player = get_num("enter max people in room: " ,100)
    min_player = get_num("enter min people in room: ", max_player)
    price_per_person = get_num("enter a price to 1 person: ", 200)
    add_room_to_list(name, difficult, duration, max_player, min_player, price_per_person)



def update_details_of_an_existing_room():
    room_num = get_num("enter room ID number", 1000)
    target_id = search_room_by_id(room_num)
    all_rooms = load_rooms()
    for room in all_rooms:
        if room["room_id"] == target_id:
            choose = str_to_int(update_rooms_menu())
            if choose == 1:
                room["name"] = get_name("enter new name")
            elif choose == 2:
                room["difficulty"] = get_difficult()
            elif choose == 3:
                room["duration"] = get_num("enter new duration", 100)
            elif choose == 4:
                room["min_players"] = get_num("enter new min players", room["max_players"])
            elif choose == 5:
                room["max_players"] = get_num("enter new max players", 20)
                if room["max_players"] < room["min_players"]:
                    break
            elif choose == 6:
                room["price_per_player"] = get_num("enter new price", 200)
            elif choose == 7:
                pass
            else:
                print("Invalid option")
                return

            dump_rooms(all_rooms)
            print("Room updated successfully!")
            return

    print("Room not found.")



def enable_or_disable_a_room():
    name = get_name("Enter name of room: ")
    rooms = load_rooms()
    for room in rooms:
        if room["name"] == name:
            room["is_active"] = not room["is_active"]
            dump_rooms(rooms)
