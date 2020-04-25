temp = 30

if temp > 30:
    print('its a hot day')
else:
    print('its not a hot day')
# #Name check
name = input('What is your name? (minimum of 3 characters): ')

if len(name) < 3:
    print('not enough characters')
elif len(name) > 50:
    print('Too many characters')
else:
    print('Hello ' + name)
#
# #Weight changer
weight = int(input('Weight:'))
unit = input('(L)b or (K)g:')
kilos = .453592
pounds = 2.20462

if unit.upper() == 'L':
    print(weight * kilos)
if unit.upper() == 'K':
    print(weight * pounds)


#while loops
x =1
while x < 10:
    print("*" * x)
    x = x + 1

