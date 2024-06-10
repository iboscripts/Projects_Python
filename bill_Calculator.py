total_bill = int(input("What is your total bill? "))

tip= input("What percentage would you like to tip? ")
tip = int(tip)/100

total_bill = total_bill + tip

people= int(input("How many people of you split the bill? "))

each_person = round(total_bill / people,3)

print(f"Each person should pay {each_person}")
