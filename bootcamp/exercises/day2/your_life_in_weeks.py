# create a program using math and f-strings that tells us how many days, weeks and months we have left if we live until 90 years old

age = int(input("What is your current age?\n"))
years_remaining = 90 - age
days_remaining =  (365 * years_remaining)
weeks_remaining = (52 * years_remaining)
months_remaining = (12 * years_remaining)

message = (f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left")
print(message)