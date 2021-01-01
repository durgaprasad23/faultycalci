numbers = [2,10,20,"DP",'D',4,3,13]
  # To draw items from loop if its of mixed type then specify type
for items in numbers:
    if type(items)== int and items > 6:
        print(items)
   