#!/usr/bin/env python3
# Created By: Boluwatife Dada
# created on March 11
# This program allows the user to enter a whole number


def factorial_calculator():
    """Calculates the factorial of a whole number entered by the user,
    with input validation using a do..while loop structure.
    """
    while True:
        try:
            user_input = input("Enter a whole number: ")
            number = int(user_input)
            if number < 0:
                print("Factorial is not defined for negative numbers.")
            elif number == 0:
                print("The factorial of 0 is 1.")
            else:
                factorial = 1
                i = 1
                while i <= number:  # Simulating do..while: execute at least once
                    factorial *= i
                    i += 1
                print(f"The factorial of {number} is {factorial}.")
                break  # Exit the loop if a valid positive number is entered
        except ValueError:
            print("Invalid input. Please enter a whole number.")
        except KeyboardInterrupt:
            print("\nOperation interrupted by the user.")
            break


if __name__ == "__main__":
    factorial_calculator()
