
            # **** SETS ****

sem_marks = [75,76,92,84,87]
dp_marks = set(sem_marks)
# print(dp_marks)

#adding values into set

dp_marks.add(100)

#removing from set

dp_marks.remove(84)

#another set e.g Internal marks

internal_marks = set([24,25,19,17,18])

print("Dp_marks:",dp_marks)

#checking whether disjoint or not

# returns true if values are unique

print("Disjoint:",dp_marks.isdisjoint(internal_marks))

#union of 2 sets
print("Union set:",dp_marks.union(internal_marks))

#adding values to internal_marks

internal_marks.add(75)

print("internal_marks:",internal_marks)

#checking whether 2 sets have common point or not intersection

print(dp_marks.intersection(internal_marks))

print(internal_marks.difference_update(dp_marks))


print(dp_marks.issubset(internal_marks))