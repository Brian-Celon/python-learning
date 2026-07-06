a = 30
b = 21
greater = a > b
less = a < b
print(greater)
print(less)

num1 = int(input("Enter a integer: "))
num2 = int(input("Enter a integer: "))

if num1 != num2:
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    elif num1 < num2:
        print(f"{num2} is greater than {num1}")
else:
    print(f"{num1} and {num2} are equal")

age = int(input("How old are you?: "))
if age > 18 and age < 60:
    print("You are eligble")
elif age < 18:
    print("You are too young")
else:
    print("you are too old")