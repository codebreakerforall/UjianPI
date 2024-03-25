from datetime import datetime, timedelta

num_days = int(input("Enter the number of days: "))

future_date = datetime.now() + timedelta(days=num_days)

day_name = future_date.strftime("%A")
day_num = future_date.strftime("%d")
month_name = future_date.strftime("%B")
year = "2024"

print(f"{day_name} on {day_num} {month_name} {year}")