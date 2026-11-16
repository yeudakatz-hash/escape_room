def reports_menu():
    choose = input("""
=================================
  Escape Room Management System
=================================

1. Total number of active bookings.
2. Total number of cancelled bookings.
3. Total revenue from active bookings.
4. Total cancellation fees from cancelled bookings.
5. The most popular room, based on the number of active bookings.
6. Number of bookings for each room.
7. Occupancy rate for a specific room on a given date.
8. Back to main menu


choose an option: 
    """)
    return choose