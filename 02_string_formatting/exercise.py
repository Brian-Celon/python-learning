
name = input("What is your name?: ")
age =  int(input("How old are you?: "))
course = input("What is you course?: ")
quiz1 = float(input("Quiz 1 score: "))
quiz2 = float(input("Quiz 2 score: "))
quiz3 = float(input("Quiz 3 score: "))

total_score =  quiz1 + quiz2 + quiz3
average = total_score / 3

print("==============================")
print("       STUDENT REPORT         ")
print("==============================")
print("\n")
print(f"Name : {name}")
print(f"Age : {age}")
print(f"Course : {course}\n")
print("Quiz Scores")
print("-----------")
print(f"Quiz 1: {quiz1}")
print(f"Quiz 2: {quiz2}")
print(f"Quiz 3: {quiz3}\n")
print(f"Total Score: {total_score}")
print(f"Average Score: {average:.2f}\n")
print("===============================")