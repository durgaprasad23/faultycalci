print("Enter the operator:")
op = input()
print("Enter 2 numbers: ")
n1 = int(input())
n2 = int(input())

if(n1 == 45 and n2 == 3 and op == "*"):
    print("result is: 555")
elif(n1 == 56 and n2 == 9 and op == "+"):
    print("reslut is: 77")
elif(n1 == 56 and n2 == 6 and op == "/"):
    print("result is: 4")    
elif(op == "*"):
    print("result:",n1*n2)
elif(op == "+"):  
    print("result:",n1+n2)
elif(op == "-"):
    print("result:",n1-n2)
elif(op == "/"):
    print("result:",n1/n2)

     
