       #**** IF_ELIF_ELSE ****
print("Enter your Name:")
name = input()
print("Enter you age:")
age = int(input())

if age > 18:
    print("you can drive "+ name +" As you age is :",age )
elif age == 18:
    print("you cannot drive "+ name +"!" +" we would like to verify you!")
else:
    print("you cannot drive "+ name +"!" + " as you are under age:",age)    
