try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    print(a/b)

except ValueError:
    print("Enter numbers only")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Calculation successful")

finally:
    print("Thank you")

#ATM PIN Validation with Error Handling
correct_pin = 1234
attempts = 3

while attempts > 0:
    try:
        pin = int(input("Enter your ATM PIN: "))

        if pin == correct_pin:
            print("PIN accepted. Access granted!")
            break

        else:
            attempts -= 1
            print("Incorrect PIN. Try again.")
            print("Attempts remaining:", attempts)

    except ValueError:
        attempts -= 1
        print("Invalid input! Please enter numbers only.")
        print("Attempts remaining:", attempts)

    finally:
        print("Transaction check completed.\n")


if attempts == 0:
    print("ATM blocked due to multiple incorrect attempts.")