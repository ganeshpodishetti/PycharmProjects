income = int(input())

if income <= 15527:
    percent = 0
    calculated_tax = 0
elif income >= 15528 and income <= 42707:
    percent = 15
    tax1 = income / 100 * percent
    calculated_tax = round(tax1)
elif income >= 42708 and income <= 132406:
    percent = 25
    tax1 = income / 100 * percent
    calculated_tax = round(tax1)
else:
    percent = 28
    tax1 = income / 100 * percent
    calculated_tax = round(tax1)

print(f"The tax for {income} is {percent}%. That is {calculated_tax} dollars!")
