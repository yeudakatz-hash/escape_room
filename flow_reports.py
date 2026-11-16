from data.booking import *




def total_number_of_active_bookings():
    count_active = 0
    all_bookings = load_booking()
    for book in all_bookings:
        if book["status"] == "Active":
            count_active += 1
    print(count_active)



def total_number_of_cancelled_bookings():
    count_cancelled = 0
    all_bookings = load_booking()
    for book in all_bookings:
        if book["status"] == "Cancelled":
            count_cancelled += 1
    print(count_cancelled)



def total_revenue_from_active_bookings():
    total = 0
    all_bookings = load_booking()
    for book in all_bookings:
        if book["status"] == "Active":
            total += book["total_price"]
    print(total)



def total_cancellation_fees_from_cancelled_bookings():
    total = 0
    all_bookings = load_booking()
    for book in all_bookings:
        total += float(book["cancellation_fee"])
    print(total)



def the_most_popular_room_based_on_the_number_of_active_bookings():
    all_dict = number_of_bookings_for_each_room()
    print(max(all_dict, key=all_dict.get))



def number_of_bookings_for_each_room():
    d = {}
    all_bookings = load_booking()
    for book in all_bookings:
        room = book["room_id"]
        if room in d:
            d[room] += 1
        else:
            d[room] = 1
    print(d)
    return d



def occupancy_rate_for_a_specific_room_on_a_given_date():
    pass