num = int(input("Give any number "))
reverse = 0
while num > 0:
    remainder = num % 10
    reverse = reverse * 10 + remainder
    num = num // 10
print("The reverse number is", str(reverse))