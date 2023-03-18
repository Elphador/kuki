a = "abc"
intial = 0 

for i in range(int(len(a)/5)+1):
    old_intial = intial
    intial += 5
    print(a[old_intial:intial])

    


