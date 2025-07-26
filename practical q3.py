monthly_saving = float(input("Enter the monthly saving amount: "))
monthly_interest_rate = 0.00417
account_value = 0.0


month = list(range(10))

print("Month    Total   ")

for month in range(1, 11):
    account_value = (account_value + monthly_saving) * (1 + monthly_interest_rate)

    if month == 1:
        month_name = "1st"
    elif month == 2:
        month_name = "2nd"
    elif month == 3:
        month_name = "3rd"
    else:
        month_name = f"{month}th"

    print(f"{month_name}    RM {account_value:7.2f}")

