
from datetime import date
today = date.today()

def greet_user(name):
    print('Hi '  + name)
    print('Welcome')
    print('Todays date is', today)

print("Start")
name = input('What is your name? ')
greet_user(name)
print("Finish") 