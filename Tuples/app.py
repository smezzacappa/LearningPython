#list []
#can change items in the list
numbers = [1 ,2, 3]

#tuples()
#cannot change items in the list
numbers2 = (1, 2, 3)
print(numbers2)

#unpacking
x, y, z, = numbers2
print(x)
total = x + y + z 
print(total)

#dictionary
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
#prints customer object
print(customer)

#prints specific attribute: CASE SENSITIVE
print(customer["name"])

#prints if specific attribute is in object
print(customer.get('name'))

#update value
customer["name"] = "Jack Smith"
print(customer["name"])

#new value
customer["birthday"] = "March 1 2000"
print(customer["birthday"])

print(customer)

#project input takes in numbers and outputs the word of the number

phone = input("Phonenumber: ")

digits_mapping = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine",
    "0" : "Zero",
}

output = ""

for char in phone:
    output += digits_mapping.get(char, "Not there") + " "
print(output)