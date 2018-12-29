n = 1
set = {1}
while n <= 20:
    i = 2
    a = 1
    while i < n:
        if n % i == 0:
            print( "数字"+ str(n) + "已经处完")
            a = 1
            break


        print(n)
        print(set)
        print(len(set))
        print(a)

        i = i + 1
        a = a + 1
        if a + 1 == n:
            set.add(n)
            print( "数字"+ str(n) + "已经处完")
        print() 
    n = n + 1
