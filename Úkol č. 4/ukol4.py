
def Prvociselnost ( num ):
    for i in num:
        if i > 1:
            for j in range(2, i):
                if (i % j) == 0:
                    print(i, "není prvočíslo")
            else:
                print(i, "je prvočíslo")
        else:
            print(i, "není prvočíslo")
    

num = [1 , 2 , 5 , 8 , 9 , 2003 , 37 , 73]
Prvociselnost(num)