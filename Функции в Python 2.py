def say_hello():
    print('hello world')
say_hello()

def say_my_name():
    num1 = 1
    num2 = 2
    sum = num1 + num2
    return sum
print(say_my_name())
print (type(say_my_name()))


def print_sum(num1, num2):
    summ = num1 + num2
    print(summ)
print_sum(3,5)

x = 5
def xyz(x):
    print(x)
    x = 2
    print(x)
print (x)
xyz(x)

z = 100
def zir():
    global z
    print (z)
zir()