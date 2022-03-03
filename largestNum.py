num1 = int(input("Give 1st number: "))
num2 = int(input("Give 2nd number: "))
num3 = int(input("Give 3rd number: "))
if num1 > num2:
    if num1 > num3:
        print("1st number is largest")
elif num2 > num3:
    print("2nd number is largest")
else:
    print("3rd number is largest")