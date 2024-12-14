def cube(num):
    return num*num*num
def check_3(num):
    if num%3==0:
        return cube(num)
    else:
        return False
num=int(input("Please enter the number"))
print(check_3(num))
