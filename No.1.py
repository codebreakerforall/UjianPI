# define the number of days in a year (2024)
days_in_year = 366

# read in a whole number
num = int(input("Enter a whole number: "))

# divide the number by the number of days in the year and display the result with 11 decimal places
result = num / days_in_year
print(format(result, '.11f'))