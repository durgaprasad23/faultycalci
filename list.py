
        #**** lISTS ****


players = ["Kobe","Lebron","Kyrie","Jordan","Harden"] #List Mutable - we can change the lists
numbers = [10,40,90,23,16,13,50]
jerseyno = (10,13,40,27,18) #Tuple immutable - we can change this

print(players)
print(numbers)
print(jerseyno)
print(players[::2]) # List with 1 skip
print(players[::-1]) # reversed list
print(players[::-2])# reversed list with 1 skip


print(numbers[::]) #display from numbers list
print(numbers[::-1]) # reversed list

# sorting of numbers list
numbers.sort()
print("SortedList:",numbers)

# reverse list
numbers.reverse()
print("Reversed list:",numbers)
#appending
numbers.append(40)
print("appended list:",numbers)

#popping from list
numbers.pop()
print("popped list:",numbers)

#inserting 30 in 3rd position
numbers.insert(3,30)
print("inserted list:",numbers)

#remove of 30 value
numbers.remove(30)
print("deleted list:",numbers)

# returns index of specific value
print(numbers.index(40))

#returns copy of a list
print(numbers.copy())

# extending the list
players.extend("Harden")
print(players)

# clearing the list
numbers.clear()

print(numbers)