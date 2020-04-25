matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#matrix modification
matrix[0][1] = 20
print(matrix[0][1])

#prints all the numbers in the matrix
for row in matrix:
    for item in row:
        print(item)


# .append()
#add number to end of list
numbers = [5, 2, 1, 7, 4]
numbers.append(20)
print(numbers)

# .insert()
#add number to specific place in list
numbers_new = [1 ,2, 5, 9, 11]
numbers_new.insert((len(numbers_new) - 1), 10)
print(numbers_new)

# .remove()
#removes specific number from list
numbers_new_two = [1 ,2, 5, 9, 11]
numbers_new_two.remove(2)
print(numbers_new_two)

# .clear()
#removes all numbers from a list
numbers_new_two = [1 ,2, 5, 9, 11]
numbers_new_two.clear()
print(numbers_new_two)

# .pop()
#removes last item from list
numbers_new_two = [1 ,2, 5, 9, 11]
numbers_new_two.pop()
print(numbers_new_two)

# .pop(x)
#removes number from place in array
numbers_new_two = [1 ,2, 5, 9, 11]
numbers_new_two.pop(3)
print(numbers_new_two)

# .index()
#returns first occurance of number
numbers_new_two = [1 ,2, 5, 9, 11]
print(numbers_new_two.index(5))

#checks for a number in the list
numbers_new_two = [1 ,2, 5, 9, 11]
print(50 in numbers_new_two)

# .count()
#counts how many times a specific number is in a list
numbers_new_two = [1 ,2, 5, 9, 5, 11]
print(numbers_new_two.count(5))

# .sort()
#sorts the numbers in the list
numbers_new_two = [12, 3, 1222, 3, 6, 2, 7, 1]
numbers_new_two.sort()
print(numbers_new_two) 

# .reverse()
#sorts the numbers in the list backwards
numbers_new_two = [12, 3, 1222, 3, 6, 2, 7, 1]
numbers_new_two.sort()
numbers_new_two.reverse()
print(numbers_new_two) 

# .copy()
#copys the numbers in a list
numbers_new_two = [12, 3, 1222, 3, 6, 2, 7, 1]
numbers_three = numbers_new_two.copy()
print(numbers_three) 

# .copy()
#copys the numbers in a list
#adds a new number to the end
numbers_new_two = [12, 3, 1222, 3, 6, 2, 7, 1]
numbers_three = numbers_new_two.copy()
numbers_three.append(50293)
print(numbers_three) 



#Removing all dupes
numbers_list = [1, 1, 2, 3, 3, 5, 6, 7, 1, 2, 3, 4, 1, 2, 3]
#initializing empty list
dupes = []

#loops through numbers_list, 
for number in numbers_list:
    #checks if number in numbers_list is in new list. If not adds it to the list, if it is, moves on to next number in the list
    if number not in dupes:
        dupes.append(number)

#prints new list without dupes
print(dupes)

