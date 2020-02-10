list = [list(range(x, x+10)) for x in range(1,100,10)]

for i in list:
    for y in i:
        print(y, end=" ")
    print('\n')
