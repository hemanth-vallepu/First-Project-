#print("--- Shopping Bill Generator ---")

while True:

    
    total_amount = 0
    discount = 0
    final_bill = 0

    
    while True:
        item_price = float(input("Enter item price: "))

        if item_price == 0:
            break

        total_amount = total_amount + item_price

    
    if total_amount > 1000:
        discount = total_amount * 10 / 100
    elif total_amount > 500:
        discount = total_amount * 5 / 100
    else:
        discount = 0

   
    final_bill = total_amount - discount

    
    print("Total Amount:", total_amount)
    print("Discount:", discount)
    print("Final Bill:", final_bill)

    
    choice = input("Do you want to continue? yes/no: ")

    if choice.lower() == "no":
        print("Thank you for shopping!")
        break