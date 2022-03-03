a = int(input(" Give any number "))
t = 0
while a > 0:
    n = a % 10
    t = t * 10 + n
    a = a // 10
    print(t)