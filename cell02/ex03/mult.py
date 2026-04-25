first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
mult = first * second
if mult > 0:
    print(f"{first} x {second} = {mult}")
    print("The result is positive.")
elif mult < 0:
    print(f"{first} x {second} = {mult}")
    print("The result is negative.")
else:
    print(f"{first} x {second} = {mult}")
    print("The result is positive and negative")