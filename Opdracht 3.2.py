def loop1():
    print("shopping cart")
    payment_method = input("Payment method? [Online/Offline] ").lower()

    pay_details = ("Enter payment details.\n"
                   "place order.")

    order_created = "Order created automatically"

    if payment_method == "online":
        print("Place order purchase")
        admin_user = input("Admin user? [Yes/No] ").lower()

        if admin_user == "no":
            approval_rules = input("Approval Rules? [Rejected/Approved] ").lower()
            if approval_rules == "rejected":
                print("Purchase Order Rejected")
            elif approval_rules == "approved":
                print(pay_details)

        elif admin_user == "yes":
            print(pay_details)
        else:
            print("Abort, unknow input")
        loop1()

    elif payment_method == "offline":
        print("Place order purchase")
        admin_user = input("Admin user? [Yes/No] ").lower()

        if admin_user == "no":
            approval_rules = input("Approval Rules? [Rejected/Approved] ").lower()
            if approval_rules == "rejected":
                print("Purchase Order Rejected")
            elif approval_rules == "approved":
                print(order_created)

        elif admin_user == "yes":
            print(order_created)
        else:
            print("Abort, unknow input")
            loop1()
    else:
        print("Abort, unknow input")
        loop1()
loop1()




