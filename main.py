"""
PowerOfTen
"""
# Provide your solution here
three_digit_number = int(input("Enter a max 3 digit number: "))

"""
Cash Box
"""
# Provide your solution here
amount_paid = int(input("To pay: "))


if amount_paid <0:
    print("Negative payment is invalid.")
    amount_paid = int(input("To pay: "))
amount_received = int(input("Received:"))


result = amount_received - amount_paid

if amount_received <0:
    print("Negative received amount is invalid.")
    amount_paid = int(input("To pay: "))
    amount_received = int(input("Received: "))
elif result < 0:
    print("You did not pay enough.")
    amount_paid = int(input("To pay: "))
    amount_received = int(input("Received: "))
elif result >= 0:
    print("Your change is", result)

