print("Welcome to the tip calculator")
Total_bill = input("What was the total bill? $")
Tip_percentage = input("How much tip would you like to give? 10, 12, or 15?")
No_of_people = input("How many people to split the bill?")

Total_billl = int(Total_bill)
Tip_percentagee = int(Tip_percentage)
No_of_peoplee = int(No_of_people)

Total_payment = Total_billl*((Tip_percentagee)/100) + Total_billl
Payment_to_be_made_by_each = round(Total_payment/5, 2)
Payment_to_be_made_by_each = "{:.2f}".format(Payment_to_be_made_by_each)
print(f"Each person should pay: ${Payment_to_be_made_by_each}")
