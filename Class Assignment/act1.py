employee = []
while True:
    try:
        print("Welcome to the Employee Management System\n")
        print("Please select an option: \n1.) Add Employee\n2.) Delete Employee\n3.) Update Employee Salary" \
        "\n4.) Show Employee list\n5.) Exit")

        option = int(input("Choice: "))

        if option == 1:
            number = int(input("How many employees do you want to enter?: "))
            for i in range(0, number):
                employee_id = input("Enter Employee ID: ")
                if i[0] == employee_id:
                    print("Invalid Employee ID\n Enter valid Employee ID")
                else:
                    employee_name = input(f"Enter Employee #{i+1} name:")
                    employee_age = int(input("Enter employee age: "))
                    employee_position = input("Enter employee position: ")
                    employee_salary = float(input("Enter Employee Salary: "))
                    employee.append([employee_id, employee_name, employee_age, employee_position, employee_salary])
                    print(employee)



        while True:
            choice = input("Do you want to continue (Y/N)?: ")
            if choice.upper() == 'Y' or choice.upper() == "N":
                if choice.upper() == 'N':
                    exit(0)
                elif choice.upper() == 'Y':
                    break
                else:
                    print("Invalid Input")
    except ValueError:
        print("Invalid input!")