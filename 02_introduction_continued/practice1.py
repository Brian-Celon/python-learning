#Shopping Receipt
name = input("What is your name?: ")
item1 = float(input("How much is the price of item 1?: "))
item2 = float(input("How much is the price of item 2?: "))
item3 = float(input("How much is the price of item 3?: "))

#Calculate
total = item1 + item2 + item3
average = (item1 + item2 + item3) /3
vat = total * 0.12
final_total = total + vat 

print("========== Customer Receipt ==========")
print(f"Customer name: {name}")
print(f"Subtotal: {total}")
print(f"VAT: {vat}")
print(f"Total: {final_total}")
print(f"\n")
print(f"Average: {average:.2f}")