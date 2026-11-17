import json
path = "data/rooms.json"




def dump_rooms(rooms_list):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(rooms_list, file, indent=2)

def load_rooms():
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        dump_rooms(rooms)
        return rooms





def get_len_rooms():
    all_rooms = load_rooms()
    len_rooms = len(all_rooms) + 1
    return f"R{len_rooms:03d}"



def search_room_by_id(num):
    new_num = str(num)
    if num < 10:
        return "R00" + new_num
    elif num < 100:
        return "R0" + new_num
    elif num < 1000:
        return "R" + new_num



def add_room_to_list(name, difficult, duration, max_player, min_player, price_per_person):
    all_rooms = load_rooms()
    new_room = {
        "room_id": get_len_rooms(),
        "name": name,
        "difficulty": difficult,
        "duration": duration,
        "min_players": min_player,
        "max_players": max_player,
        "price_per_player": price_per_person,
        "is_active": True
    }
    all_rooms.append(new_room)
    dump_rooms(all_rooms)