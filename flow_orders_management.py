from validations.name import *
from validations.num import *
from validations.time import *
from data.booking import *
from menu.update_menus import update_order_menu
from flow_rooms_management import view_full_details_of_a_specific_room



def creating_a_new_order():
    details_room = view_full_details_of_a_specific_room()
    while details_room is None:
        details_room = view_full_details_of_a_specific_room()
    room, id_room, price_per_person, max_players, min_players = details_room.get("name"), details_room.get("room_id"), details_room.get("price_per_player"), details_room.get("max_players"), details_room.get("min_players")
    players = get_num("num of players: ", 100)
    if not details_room["is_active"] or not min_players <= players <= max_players:
        print("error")
        return
    date = get_date()
    time = get_time()
    name = get_name("enter your name: ")
    add_booking_to_list(name, id_room, room, date, time, players, price_per_person)



def viewing_all_orders():
    for order in load_booking():
        print(order)
    return



def searching_for_an_order_by_id():
    id_order = search_order_by_id(get_num("enter id to search order", 1000))
    for order in load_booking():
        if order["booking_id"] == id_order:
            print(order)



def viewing_orders_for_a_specific_customer():
    name_order = get_name("Enter name order to search")
    for order in load_booking():
        if order["customer_name"].lower() == name_order:
            print(order)



def viewing_orders_by_date():
    booking_list = load_booking()
    print(sorted(booking_list, key=lambda x: datetime.strptime(x['booking_date'], '%Y-%m-%d')))



def modifying_the_details_of_an_existing_order():
    order_num = get_num("enter booking ID number", 1000)
    target_id = search_order_by_id(order_num)
    all_bookings = load_booking()
    for book in all_bookings:
        if book["booking_id"] == target_id:
            choose = str_to_int(update_order_menu())
            if choose == 1:
                book["customer_name"] = get_name("enter new customer name")
            elif choose == 2:
                new_room_num = get_num("enter new room ID number", 1000)
                book["room_id"] = f"R{new_room_num:03d}"
            elif choose == 3:
                pass
            elif choose == 4:
                pass
            elif choose == 5:
                book["players"] = get_num("enter new number of players", 50)
                # book["total_price"] = calculate_price(book["players"], book[""], book[""])
            else:
                print("Invalid option")
                return
            dump_booking(all_bookings)
            print("Order updated successfully!")
            return
    print("Order not found.")



def canceling_an_order():
    num = get_num("Enter num of book: ", 1000)
    real_id = search_order_by_id(num)
    books = load_booking()
    for book in books:
        if book["booking_id"] == real_id:
            if book["status"] == "Active":
                print("the book is also cancelled")
                return
            book["status"] = "Cancelled"
            book["cancellation_fee"] = book["total_price"] * 0.5
            dump_booking(books)
