print("Welcome to the tip calculator!")
total_bill = int(input("What was the total bill? $"))
tip_rate = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
print(
    "Each person should pay: "
    + str((total_bill + (total_bill * tip_rate / 100)) / people)
)
