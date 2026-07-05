#type conversion is essenstially the changing of one data type to another 
#This is done implicitly or explicitly

name = "Brian"
age = 21 #python automatically converts 

#type casting is where you convert it
age = input("How old are you?: ")
year = int(input("What year is it?: "))
birth_year = year - int(age)
print(f"Your birth year is: {birth_year}")