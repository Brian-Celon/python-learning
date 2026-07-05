#Even or Odd Checking

number = int(input("Enter a whole number: "))

if number % 2:
    print(f"{number} is an odd number")
else:
    print(f"{number} is an even number")

#Age Category 

age = int(input("How old are you?: "))

if age < 0:
    print("Invalid input, please enter an even whole number")
elif age <=12:
    print("You are a child")
elif age <=17:
    print("You are a teenager")
elif age <= 59:
    print("You are an adult")
else:
    print("You are a senior")
