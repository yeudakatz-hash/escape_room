def orders_management_menu():
    choose = input("""
=================================
  Escape Room Management System
=================================

1. Creating a new order.
2. Viewing all orders.
3. Searching for an order by ID.
4. Viewing orders for a specific customer.
5. Viewing orders by date.
6. Modifying the details of an existing order.
7. Canceling an order.
8. Back to main menu

choose an option: 
""")
    return choose