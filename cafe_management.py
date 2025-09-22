import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

# Load menu from CSV
menu_df = pd.read_excel(r'c:\Users\Pc\Desktop\cafe managment system.py\menucard.xlsx.xlsx')
menu_df.set_index('ID', inplace=True)

order_history = []

# Show menu
def show_menu():
    print("\n===== Café Menu =====")
    print(menu_df.to_string(index=True))
    print("======================\n")

# Take order
def take_order():
    order = []
    total = 0
    while True:
        try:
            item_id = int(input("Enter item number to order (or 0 to finish): "))
            if item_id == 0:
                break
            if item_id not in menu_df.index:
                print("Invalid item number.")
                continue
            item_name = menu_df.loc[item_id, 'ITEMS']
            price = menu_df.loc[item_id, 'PRICE']
            quantity = int(input(f"Enter quantity of {item_name}: "))
            item_total = price * quantity
            order.append((item_name, quantity, item_total))
            total += item_total
        except ValueError:
            print("Please enter valid numbers.")
    return order, total


# Show bill
def show_bill(order, total):
    print("\n===== Bill =====")
    for item_name, quantity, item_total in order:
        print(f"{item_name} x{quantity} = ₹{item_total}")
    print("------------------")
    print(f"Total: ₹{total}")
    print("==================")

# Save order
def save_order(order, total):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for item_name, quantity, item_total in order:
        order_history.append({
            'Time': time,
            'Item': item_name,
            'Quantity': quantity,
            'Total': item_total
        })

# View sales summary
def sales_summary():
    if not order_history:
        print("No sales data available.")
        return
    df = pd.DataFrame(order_history)
    summary = df.groupby('Item')['Quantity'].sum().reset_index()
    print("\n===== Sales Summary =====")
    print(summary.to_string(index=False))

    # Plot
    plt.figure(figsize=(8, 5))
    plt.bar(summary['Item'], summary['Quantity'], color='skyblue')
    plt.xlabel('Items')
    plt.ylabel('Total Quantity Sold')
    plt.title('Item Sales Report')
    plt.tight_layout()
    plt.show()



# Main loop
def main():
    while True:
        print("\n1. Show Menu")
        print("2. Take Order")
        print("3. View Sales Summary")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            show_menu()
        elif choice == '2':
            show_menu()
            order, total = take_order()
            if order:
                show_bill(order, total)
                save_order(order, total)
        elif choice == '3':
            sales_summary()
        elif choice == '4':
            print("Thank you for using Café Management System!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the app
main()
