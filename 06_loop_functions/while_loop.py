#Bar activity
customer = int(input("How many customers are there?: "))

for i in range(1, customer +1):
    age = int(input(f"Customer #{i} age: "))
    while age <= 18:
        if age <= 18:
            print("You are a minor")
            break
        
    
        