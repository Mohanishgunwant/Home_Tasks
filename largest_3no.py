a=input("Enter the first number\n")
b=input("Enter the second number\n")
c=input("Enter the third number\n")
if (a>=b) and (a>=c):
    largest=a
elif (b>=a) and (b>=c):
    largest=b
else:
    largest=c
print("The largest of numbers",a,",",b,",",c,"is",largest)
