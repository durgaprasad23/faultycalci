roll_nos = [2,3,5,6,8,9,11,13,25,35,45,65,15,16,18,17,19,"twenty-four","thirty-two"]
print("Printing th list:",roll_nos)

cse = {"Akki":1,"Dp":16,"Manasa":18,"Vishwa":27}
print("The class is:",cse)

# if we want to access the elemets one after another and if they are greater than 5 and less that 17 print them
for items in roll_nos:
    if type(items)== int and items > 5 and items < 16:
        print(items)

print(" ")
# accessing data from dict-cse

for i,values in cse.items():  # to access the values for key u need to specify .items()
    if(values == 1 or values == 16):
        print(i)