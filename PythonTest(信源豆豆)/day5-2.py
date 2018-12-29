n = 1
set = {1}
while n <= 100:
    i = 2
    a = 1
    while i < n:
        if n % i == 0:
            a = 1
            break

        i = i + 1
        a = a + 1
        if a + 1 == n:
            set.add(n)
    n = n + 1
print(set)