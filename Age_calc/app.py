from datetime import date

birth_year = input('What is you birth year? ')
year = date.today().year
age = (int(year) - int(birth_year))
print(age)

weight = input('What is you weight in lbs? ')
kilos = (int(weight)/2.205)

print(kilos)