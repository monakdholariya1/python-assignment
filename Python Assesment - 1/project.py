# Store all orders in nested dictionary
orders = {}  



# Record new repair order
def repair_order_show(order_id, customer_name, device_type, issue, due_date):
    orders[order_id] = {
        "customer_name": customer_name,
        "device_type": device_type,
        "issue": issue,
        "due_date": due_date
    }



#print all record order for new repair order
    print("\n===========ORDER RECORDED==============")
    print(f"Order ID      : {order_id}")
    print(f"Customer Name : {customer_name}")
    print(f"Device Type   : {device_type}")
    print(f"Issue         : {issue}")
    print(f"Due Date      : {due_date}")
    print("--------------------------------------")
    print("Repair order details recorded.\n")


# Generate bill for an order
def genarator_bill():


#orders is not found then if block is executed
    if not orders:
        print("No orders found. Please record an order first.")


#enter your order_id
    order_id = input("Enter Order ID to generate bill: ")



#in orders is available order_id if block is executed
    if order_id in orders:
        try:
            replace_part = input("Enter the part replaced: ")
            repair_fees = float(input("Enter repair fees: "))
            discount = float(input("Enter discount: "))
            tax = repair_fees * 0.18
            total_fees = repair_fees + tax - discount
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            return

        print("--------------------------------")
        print(f"Parts replaced : {replace_part}")
        print(f"Repair fees    : ₹{repair_fees:.2f}")
        print(f"Tax (18%)      : ₹{tax:.2f}")
        print(f"Discount       : ₹{discount:.2f}")
        print("================================")
        print(f"TOTAL          : ₹{total_fees:.2f}")
        print("================================\n")
    else:
        print("Order ID not found!")


# Menu loop
while True:
    print("1. Record new order")
    print("2. Generate bill")
    print("3. Exit\n")


#choice your input 
    choice = input("Enter your choice: ")


# If user selects 1 -> record new order
    if choice == "1":
        order_id = input("Enter Order ID: ")
        customer_name = input("Enter customer name: ")
        device_type = input("Enter device type: ")
        issue = input("Enter issue: ")
        due_date = input("Enter due date (DD/MM/YYYY): ")
        repair_order_show(order_id, customer_name, device_type, issue, due_date)


# If user selects 2 -> generate bill
    elif choice == "2":
        genarator_bill()


# If user selects 3 -> exit program
    elif choice == "3":
        print("Exiting. Goodbye!")
        break


#if user selects 4 -> invalid choice
    else:
        print("Invalid choice. Enter 1-3.")
