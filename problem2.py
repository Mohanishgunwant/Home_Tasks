
#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

def list_divisor(x):
    lis = []
    for i in range(1,x+1):
        if x % i == 0:
            lis.append(i)
    print(lis)
list_divisor(int(input("Enter the number\n")))
