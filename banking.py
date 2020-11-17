# Write your code here
import random


class CardAnatomy:
    def __init__(self):
        self.acc_num = None  # account number
        self.acc_pin = None  # account pin
        self.choice = None

    def create_account(self):
        random.seed(100)
        self.acc_num = random.randrange()

    def checksum(self):



def login_screen():
    print(f'1. Create an account')
    print(f'2. Log into account')
    print(f'0. Exit')


def main():
    while True:
        card = CardAnatomy()
        login_screen()
        choice = int(input("\n"))
        if choice == 1:
            card.create_account()


if __name__ == '__main__':
    main()
