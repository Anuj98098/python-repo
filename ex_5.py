# Here we will ask the users to enter their age and assuming average life of a human 90 years
age=int(input("Enter your age: "))

years_left=90-age
days_left=years_left*365
months_left=years_left*12

print(f"you have {days_left} days and {months_left} and {years_left}")