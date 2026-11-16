from flow_rooms_management import *
from flow_orders_management import *
from flow_reports import *
from menu.rooms_management_menu import *
from menu.orders_management_menu import *
from menu.reports_menu import *



def escape_zone_rooms_management():
    flag = True
    while flag:
        choose = rooms_management_menu()
        if choose == "1":
            view_all_rooms()
        elif choose == "2":
            view_full_details_of_a_specific_room()
        elif choose == "3":
            add_a_new_room()
        elif choose == "4":
            update_details_of_an_existing_room()
        elif choose == "5":
            enable_or_disable_a_room()
        elif choose == "6":
            flag = False
        flag = False



def order_management():
    flag = True
    while flag:
        choose = orders_management_menu()
        if choose == "1":
            creating_a_new_order()
        elif choose == "2":
            viewing_all_orders()
        elif choose == "3":
            searching_for_an_order_by_id()
        elif choose == "4":
            viewing_orders_for_a_specific_customer()
        elif choose == "5":
            viewing_orders_by_date()
        elif choose == "6":
            modifying_the_details_of_an_existing_order()
        elif choose == "7":
            canceling_an_order()
        elif choose == "8":
            flag = False
        flag = False



def reports():
    flag = True
    while flag:
        choose = reports_menu()
        if choose == "1":
            total_number_of_active_bookings()
        elif choose == "2":
            total_number_of_cancelled_bookings()
        elif choose == "3":
            total_revenue_from_active_bookings()
        elif choose == "4":
            total_cancellation_fees_from_cancelled_bookings()
        elif choose == "5":
            the_most_popular_room_based_on_the_number_of_active_bookings()
        elif choose == "6":
            number_of_bookings_for_each_room()
        elif choose == "7":
            occupancy_rate_for_a_specific_room_on_a_given_date()
        elif choose == "8":
            flag = False
        flag = False