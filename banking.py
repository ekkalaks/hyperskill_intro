# Write your code here
import random
num1 = 4
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0
num7 = None
num8 = None
num9 = None
num10 = None
num11 = None
num12 = None
pin1 = None
pin2 = None
pin3 = None
pin4 = None


def create_card():
    global num7, num8, num9, num10, num11, num12
    random.seed()
    num7 = random.randint(0, 9)
    num8 = random.randint(0, 9)
    num9 = random.randint(0, 9)
    num10 = random.randint(0, 9)
    num11 = random.randint(0, 9)
    num12 = random.randint(0, 9)


def create_pin():
    random.seed()
    global pin1, pin2, pin3, pin4
    pin1 = random.randint(0, 9)
    pin2 = random.randint(0, 9)
    pin3 = random.randint(0, 9)
    pin4 = random.randint(0, 9)


def login_screen():
    print(f'1. Create an account')
    print(f'2. Log into account')
    print(f'0. Exit')


def main():
    while True:
        login_screen()
        choice = input(">")
        if choice == "1":
            create_card()
            create_pin()
            print(f'Your card number:')
            print(str(num1) + str(num2) + str(num3) + str(num4) + str(num5) + str(num6) +
                  str(num7) + str(num8) + str(num9) + str(num10) + str(num11) + str(num12))
            print(f'Your card PIN:')
            print(str(pin1) + str(pin2) + str(pin3) + str(pin4) + "\n")

        elif choice == "2":
            user_account = input(f'Enter your card number:\n' + f'>')
            user_pin = input(f'Enter your PIN:\n' + f'>')
            if (user_account[0] == str(num1)) and (user_account[1] == str(num2)) and (user_account[2] == str(num3)) \
                    and (user_account[3] == str(num4)) and (user_account[4] == str(num5)) \
                    and (user_account[5] == str(num6)) and (user_account[6] == str(num7)) \
                    and (user_account[7] == str(num8)) and (user_account[8] == str(num9)) \
                    and (user_account[9] == str(num10)) and (user_account[10] == str(num11)) \
                    and (user_account[11] == str(num12)) and (user_pin[0] == str(pin1))\
                    and (user_pin[1] == str(pin2)) and (user_pin[2] == str(pin3))\
                    and (user_pin[3] == str(pin4)):
                print("You have successfully logged in!\n")
            else:
                print(f'Wrong card number or PIN!\n')

        elif choice == "0":
            print(f'Bye!')
            return False

        else:
            print(f'Wrong Input!!! Try again!!!\n')


if __name__ == '__main__':
    main()
