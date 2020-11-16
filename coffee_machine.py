# the coffee machine has $550,
# 400 ml of water,
# 540 ml of milk,
# 120 g of coffee beans,
# and 9 disposable cups.
""""
For one espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans. It costs $4.
For a latte, the coffee machine needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7.
And for a cappuccino, the coffee machine needs 200 ml of water, 100 ml of milk, and 12 g of coffee. It costs $6.
"""


class CoffeeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.money = 550
        self.cups = 9
        self.remaining_screen()

    def remaining_screen(self):
        return f"\n" \
               f"The coffee machine has:\n" \
               f"{self.water} of water\n" \
               f"{self.milk} of milk\n" \
               f"{self.coffee} of coffee beans\n" \
               f"{self.cups} of disposable cups\n" \
               f"{self.money} of money\n"

    def buy_coffee(self, choice):
        if choice == 1:
            if (self.water < 250) and (self.coffee >= 16) and (self.cups >= 1):
                print("Sorry, not enough water!")
            elif (self.water >= 250) and (self.coffee < 16) and (self.cups >= 1):
                print("Sorry, not enough coffee beans!")
            elif (self.water >= 250) and (self.coffee >= 16) and (self.cups < 1):
                print("Sorry, not enough cups!")
            elif (self.water >= 250) and (self.coffee >= 16) and (self.cups >= 1):
                print("I have enough resources, making you a coffee!")
                self.water -= 250
                self.coffee -= 16
                self.money += 4
                self.cups -= 1

        elif choice == 2:
            if (self.water < 350) and (self.coffee >= 20) and (self.cups >= 1) and (self.milk >= 75):
                print("Sorry, not enough water!")
            elif (self.water >= 350) and (self.coffee < 20) and (self.cups >= 1) and (self.milk >= 75):
                print("Sorry, not enough coffee beans!")
            elif (self.water >= 350) and (self.coffee >= 20) and (self.cups < 1) and (self.milk < 75):
                print("Sorry, not enough cups!")
            elif (self.water >= 350) and (self.coffee >= 20) and (self.cups >= 1) and (self.milk < 75):
                print("Sorry, not enough milk!")
            elif (self.water >= 350) and (self.coffee >= 20) and (self.cups >= 1) and (self.milk >= 75):
                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.coffee -= 20
                self.money += 7
                self.cups -= 1

        elif choice == 3:
            if (self.water < 200) and (self.coffee >= 12) and (self.cups >= 1) and (self.milk >= 100):
                print("Sorry, not enough water!")
            elif (self.water >= 200) and (self.coffee < 12) and (self.cups >= 1) and (self.milk >= 100):
                print("Sorry, not enough coffee beans!")
            elif (self.water >= 200) and (self.coffee >= 12) and (self.cups < 1) and (self.milk < 100):
                print("Sorry, not enough cups!")
            elif (self.water >= 200) and (self.coffee >= 12) and (self.cups >= 1) and (self.milk < 100):
                print("Sorry, not enough milk!")
            elif (self.water >= 200) and (self.coffee >= 12) and (self.cups >= 1) and (self.milk >= 100):
                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.coffee -= 12
                self.money += 6
                self.cups -= 1

    def take_money(self):
        print(f'I gave you ${self.money}')
        self.money -= self.money


def main():
    x = CoffeeMachine()
    while True:
        command = input(f'Write action (buy, fill, take, remaining, exit):\n')
        if command == "remaining":
            print(x.remaining_screen())
        elif command == "buy":
            y = input(f'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')
            if y == "1":
                x.buy_coffee(1)
            elif y == "2":
                x.buy_coffee(2)
            elif y == "3":
                x.buy_coffee(3)
            elif y == "back":
                pass
            else:
                print("Not in list")

        elif command == "take":
            x.take_money()
        elif command == "fill":
            x.water += int(input(f'Write how many ml of water do you want to add:\n'))
            x.milk += int(input(f'Write how many ml of milk do you want to add:\n'))
            x.coffee += int(input(f'Write how many grams of coffee beans do you want to add:\n'))
            x.cups += int(input(f'Write how many disposable cups of coffee do you want to add:\n'))

        elif command == "exit":
            return False


if __name__ == '__main__':
    main()

# coffee = CoffeeMachine()
# print(coffee.buy_coffee(4))
# print(coffee.remaining_screen())
# coffee.fill_action()
