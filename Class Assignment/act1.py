employee = []
while True:
    try:
        print("Welcome to the Employee Management System\n")
        print("Please select an option: \n1.) Add Employee\n2.) Delete Employee\n3.) Update Employee Salary" \
        "\n4.) Show Employee list\n5.) Exit")

        option = int(input("Choice: "))

        if option == 1:
            id = input("Please enter Employee ID: ")
            for i in employee:
                if i[0] == id:
                    print("Duplicate ID Found!")
                    print("Enter a valid ID")
                    break
                else:
                    name = input("Enter Employee Name: ")
                    age = int(input("Enter Employee Age: "))
                    position = input("Enter Employee position: ")
                    salary = float(input("Enter Employee Salary: "))
                    employee.append([id, name, age, position, salary])
                    print(employee)



        
        choice = input("Do you want to continue (Y/N)?: ")
        if choice.upper() == 'Y' or choice.upper() == "N":
            if choice.upper() == 'n':
                exit(0)
            elif choice.upper() == 'y':
                break
            else:
                print("Invalid Input")
    except ValueError:
        print("Invalid input!")