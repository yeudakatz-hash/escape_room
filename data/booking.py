import json




path = "data/booking.json"


def dump_booking(booking_list):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(booking_list, file, indent=2)

def load_booking():
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        dump_booking(booking)
        return booking




def get_len():
    all_books = load_booking()
    len_books = len(all_books) + 1
    return f"B{len_books:03d}"


def search_order_by_id(num):
    new_num = str(num)
    if num < 10:
        return "B00" + new_num
    elif num < 100:
        return "B0" + new_num
    elif num < 1000:
        return "B" + new_num



def calculate_price(people, price_per_person, day):
    price = 0
    if 5 > people: price = people * price_per_person
    elif 5 <= people <= 6: price = price_per_person * people * 0.9
    elif people > 6: price = price_per_person * people * 0.85
    if day == 6 or day == 7: price *= 1.15
    return round(price, 2)



def add_booking_to_list(name, id_room, room, date, time, players, price_per_person):
    all_booking = load_booking()
    all_booking.append({
        "booking_id": get_len(),
        "customer_name": name,
        "room_id": id_room,
        "booking_date": date,
        "start_time": time,
        "players": players,
        # צריך עדכון של היום ולעדכן בפונקציה שלפני את מספורי הימים
        "total_price": calculate_price(players, price_per_person, 4),
        "status": "Active",
        "cancellation_fee": 0.00
    })
    dump_booking(all_booking)