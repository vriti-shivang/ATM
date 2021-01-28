# CREATED BY:- VRITI SHIVANG
# LAST EDITED ON :- 28 JAN. 2021
# STATUS :- WORKING ON IT
# PROBLEMS:- USER CAN DO ONLY ONE TRANSITION IN DEPOSIT AND WITHDRAW AND THE CODE BREAKS IF WE GIVE "STRING" AT THE PLACE OF INT OR FLOAT
# SOLUTION:- THINKING ABOUT THE SOLUTION TO MAKE MULTIPLE TRANSITION AND I HAVE TO ADD "TRY AND EXPECT" TO GET DATA IN INT OR FLOAT
print("""CREATED BY:- VRITI SHIVANG
        LAST EDITED ON :- 28 JAN. 2021""")

##############################################

# IMPORTING MODULES

import time
import datetime

###############################################

# SHOWING DATE AND TIME
present_time = datetime.datetime.now()
print(present_time.strftime("Date: %Y-%m-%d "))
print(present_time.strftime("Time: %H:%M:%S"))

################################################

# TOTAL TIME SPENT
start = time.time()


###############################################


# Creating a class (Atm)
class Atm:

    # INITIALIZING THE CLASS USING __init__
    def __init__(self):
        self._code = ""
        self.__balance = 0.00

        self.menu()

    # DEFINING THE "MENU" METHOD
    def menu(self):

        user_input = input("""How would you like to proceed?
        1.Press '1' to  enter your pin
        2.Press '2' to deposit money
        3.Press '3' to withdraw money
        4.Press '4' to check balance
        5.Press '5' to update Pin
        6.Press '6' to exit

         """)

        if user_input == "1":
            self.pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        elif user_input == "6":
            print("Have a nice day!!!")
        elif user_input == "5":
            self.update_password()
        else:
            print("Choose a valid choice")

            # RETURNS THE "MENU METHOD" WHEN THE WRONG CHOICE IS CHOSEN

            self.menu()

    # RECALL THE "PIN" METHOD  AS PER THE CHOICE

    def pin(self):
        pin = input("Enter your pin: ")
        self._code = input("Re-enter your pin: ")

        if pin == self._code:
            print("Pin is successfully changed")
            self.menu()

            # SHOWING DATE AND TIME

            current_time = datetime.datetime.now()
            print(current_time.strftime("Date: %Y-%m-%d "))
            print(current_time.strftime("Time: %H:%M:%S"))

        else:

            print("Pin does not match")

            # SHOWING DATE AND TIME

            current_time = datetime.datetime.now()
            print(current_time.strftime("Date: %Y-%m-%d "))
            print(current_time.strftime("Time: %H:%M:%S"))

            self.menu()

    # RECALL THE "DEPOSIT" METHOD  AS PER THE CHOICE

    def deposit(self):
        pin = input("Enter Your pin: ")
        if pin == self._code:
            amount_to_deposit = float(input("Enter the amount to be deposited: "))
            self.__balance = self.__balance + amount_to_deposit
            print("Amount in your account is RS.", self.__balance)

            # SHOWING DATE AND TIME

            current_time = datetime.datetime.now()
            print(current_time.strftime("Date: %Y-%m-%d "))
            print(current_time.strftime("Time: %H:%M:%S"))
            self.menu()
        else:

            print("Your pin does not match")
            self.menu()

            # SHOWING DATE AND TIME

            current_time = datetime.datetime.now()
            print(current_time.strftime("Date: %Y-%m-%d "))
            print(current_time.strftime("Time: %H:%M:%S"))

    # RECALL THE "WITHDRAW" METHOD  AS PER THE CHOICE

    def withdraw(self):
        pin = input("Enter Your pin: ")
        if self._code == pin:

            amount_to_withdraw = float(input("Enter the amount to withdraw: "))

            if self.__balance >= amount_to_withdraw:
                print("Amount left=", (self.__balance - amount_to_withdraw))

                # SHOWING DATE AND TIME

                current_time = datetime.datetime.now()
                print(current_time.strftime("Date: %Y-%m-%d "))
                print(current_time.strftime("Time: %H:%M:%S"))
                self.menu()
            else:

                print("You don't have", amount_to_withdraw)
                print("you have ", self.__balance, "in your account")

                # SHOWING DATE AND TIME

                current_time = datetime.datetime.now()
                print(current_time.strftime("Date: %Y-%m-%d "))
                print(current_time.strftime("Time: %H:%M:%S"))
                self.menu()
        else:
            print("Pin does not match")

            # SHOWING DATE AND TIME

            current_time = datetime.datetime.now()
            print(current_time.strftime("Date: %Y-%m-%d "))
            print(current_time.strftime("Time: %H:%M:%S"))
            self.menu()

    # RECALL THE "CHECK_BALANCE" METHOD  AS PER THE CHOICE

    def check_balance(self):
        pin = input("Enter your pin: ")

        if pin == self._code:

            print("Your balance in account is :", self.__balance)

            # SHOWING DATE AND TIME

            current_time = datetime.datetime.now()
            print(current_time.strftime("Date: %Y-%m-%d "))
            print(current_time.strftime("Time: %H:%M:%S"))
            self.menu()
        else:

            print("You entered wrong pin")

            # SHOWING DATE AND TIME
            current_time = datetime.datetime.now()
            print(current_time.strftime("Date: %Y-%m-%d "))
            print(current_time.strftime("Time: %H:%M:%S"))
            self.menu()

    # RECALL THE "CHECK_BALANCE" METHOD  AS PER THE CHOICE

    def update_password(self):
        last_pin = input("Enter the last pin: ")

        if last_pin != self._code:

            print("you have one more chance to update your Pin")
            last_pin = input("Enter the last pin: ")

            if last_pin != self._code:

                print("You entered the wrong pin ")

                # SHOWING DATE AND TIME

                current_time = datetime.datetime.now()
                print(current_time.strftime("Date: %Y-%m-%d "))
                print(current_time.strftime("Time: %H:%M:%S"))
                self.menu()

            else:

                print("Pin is updated successfully")
                # SHOWING DATE AND TIME
                current_time = datetime.datetime.now()
                print(current_time.strftime("Date: %Y-%m-%d "))
                print(current_time.strftime("Time: %H:%M:%S"))
                self.menu()
        else:

            print("Pin is updated successfully")
            current_time = datetime.datetime.now()
            print(current_time.strftime("Date: %Y-%m-%d "))
            print(current_time.strftime("Time: %H:%M:%S"))

            self.menu()


# CALLING THE FUNCTION
bank = Atm()

# GETTING THE TOTAL TIME SPEND
end = time.time()
print("You spend", int(end - start), "seconds")
