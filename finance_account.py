"""

Name: Hernan Ramoz

Course: ADD-100

Project: Finance Flow

Description:

This class stores income, expenses, and debt payments.

It calculates the monthly balance and displays a simple summary.

"""

class FinanceAccount:

    def __init__(self, income, expenses, debt):

        self.__income = income

        self.__expenses = expenses

        self.__debt = debt

    # getters

    def get_income(self):

        return self.__income

    def get_expenses(self):

        return self.__expenses

    def get_debt(self):

        return self.__debt

    # setters

    def set_income(self, new_income):

        self.__income = new_income

    def set_expenses(self, new_expenses):

        self.__expenses = new_expenses

    def set_debt(self, new_debt):

        self.__debt = new_debt

    # calculate balance

    def calculate_balance(self):

        return self.__income - self.__expenses - self.__debt

    # display summary

    def display_summary(self):

        balance = self.calculate_balance()

        print("\n----- Financial Summary -----")

        print("Monthly income:", self.__income)

        print("Monthly expenses:", self.__expenses)

        print("Monthly debt payments:", self.__debt)

        print("Money left after expenses and debt:", balance)

        if balance < 0:

            print("Warning: You are spending more than you earn.")

        elif balance == 0:

            print("You have no money left this month.")

        else:

            print("Good job! You still have money left.")