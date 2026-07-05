#Student Enrollment Eligibility System

full_name = input("What is your full name?: ")
age = int(input("How old are you?: "))
course = input("What is your course?: ")
score = float(input("Entrance Exam Score: "))

print("====================================")
print("        STUDENT INFORMATION        ")
print("====================================\n")

print(f"Name          : {full_name}")
print(f"Age           : {age}")
print(f"Course        : {course}")
print(f"Score         : {score}")
name_length = len(full_name)
print(f"Name Length   : {name_length}")
rounded_score = round(score)
print(f"Rounded Score : {rounded_score}\n")


if age <= 17:
    print("Not Eligible\n")
    print("Reason: ")
    print("Applicant must be at least 17 years old.")
else:
    if score <= 75:
        print("Not Qualified")
    elif score <=89:
        print("Qualified")
    elif score <=100:
        print("Qualified with Honors")
        if score >= 95:
            print("Scholarship Awarded")
        else:
            print("No Scholarship")


print("==================================== \n")