#Python practice Exercise 1: Student Information Program

print("#### Student Information Program ####")
name = input("What is your name?: ")
age = int(input("How old are you?: "))
course = input("What is your course?: ")
height = float(input("How tall are you (cm)?: "))
weight = float(input("How much do you weight (kg)?: "))

age_next_year = age + 1
height_in_meters = height / 100
bmi = weight / (height_in_meters**2)
print("Student Information: ")
print(f"""Student name: {name} \n
      Age: {age} \n
      Course: {course} \n
      Height: {height} \n
      Weight: {weight} \n
      Age next year: {age_next_year} \n
      Height in meters: {height_in_meters} \n
      BMI: {bmi.}
      """)