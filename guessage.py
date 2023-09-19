s=0
l=100
for i in range(1,9):
    age=int((s+l)/2)
    answer=input("are you " + str(age) + " years old =")
    if answer=='correct':
        print("Nice")
        break
    elif answer=='less':
        l=age
    elif answer=='more':
        s=age
    else:
        print(" its wrong answer")
        
