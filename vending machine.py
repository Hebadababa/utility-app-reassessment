# ASCII art representing the name of the application
print("""
██╗░░░██╗███████╗███╗░░██╗██████╗░██╗███╗░░██╗░██████╗░  ███╗░░░███╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗███████╗
██║░░░██║██╔════╝████╗░██║██╔══██╗██║████╗░██║██╔════╝░  ████╗░████║██╔══██╗██╔══██╗██║░░██║██║████╗░██║██╔════╝
╚██╗░██╔╝█████╗░░██╔██╗██║██║░░██║██║██╔██╗██║██║░░██╗░  ██╔████╔██║███████║██║░░╚═╝███████║██║██╔██╗██║█████╗░░
░╚████╔╝░██╔══╝░░██║╚████║██║░░██║██║██║╚████║██║░░╚██╗  ██║╚██╔╝██║██╔══██║██║░░██╗██╔══██║██║██║╚████║██╔══╝░░
░░╚██╔╝░░███████╗██║░╚███║██████╔╝██║██║░╚███║╚██████╔╝  ██║░╚═╝░██║██║░░██║╚█████╔╝██║░░██║██║██║░╚███║███████╗
░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝""")

class VendingMachine:
    def __init__(self):
        self.balance = 0
        self.items = [
            {'code': 0, 'name': 'Salad chips', 'price': 1.50, 'quantity': 5},
            {'code': 1, 'name': 'Chocolate bar', 'price': 3.00, 'quantity': 10},
            {'code': 2, 'name': 'Coke', 'price': 2.50, 'quantity': 7},
            {'code': 3, 'name': 'Iced tea', 'price': 4.00, 'quantity': 3},
            {'code': 4, 'name': 'Masafi water', 'price': 1.00, 'quantity': 8},
            {'code': 5, 'name': 'Pringles', 'price': 4.00, 'quantity': 6},
            {'code': 6, 'name': 'Candy', 'price': 0.50, 'quantity': 15}
        ]

    def display_items(self):
        print("Available items:")
        for item in self.items:
            print(f"{item['code']}. {item['name']} - ${item['price']:.2f} - Quantity: {item['quantity']}")

    def insert_money(self, amount):
        self.balance += amount
        print(f"Inserted: ${amount:.2f}, Total Balance: ${self.balance:.2f}")

    def purchase_item(self, item_code):
        item = next((item for item in self.items if item['code'] == int(item_code)), None)
        if item:
            if item['quantity'] > 0 and self.balance >= item['price']:
                self.balance -= item['price']
                item['quantity'] -= 1
                print(f"Purchased {item['name']} for ${item['price']:.2f}. Remaining Balance: ${self.balance:.2f}")
            else:
                print("Insufficient balance or item out of stock.")
        else:
            print("Invalid item code.")

    def return_change(self):
        if self.balance > 0:
            print(f"Returning change: ${self.balance:.2f}")
            self.balance = 0


def main():
    vending_machine = VendingMachine()

    while True:
        print("\nOptions:")
        print("1. Display Items")
        print("2. Insert Money")
        print("3. Purchase Item")
        print("4. Return Change")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            vending_machine.display_items()
        elif choice == '2':
            amount = float(input("Enter the amount to insert: $"))
            vending_machine.insert_money(amount)
        elif choice == '3':
            item_code = input("Enter the item code: ")
            vending_machine.purchase_item(item_code)
        elif choice == '4':
            vending_machine.return_change()
        elif choice == '5':
            break
        else:
            print("Invalid . Please try again.")


if __name__ == "__main__":
    main()