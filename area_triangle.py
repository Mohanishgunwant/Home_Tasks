a=float(input("Enter dimension of side1\n"))
b=float(input("Enter dimension of side2\n"))
c=float(input("Enter dimension of side3\n"))
s=(a+b+c)/2
area_triangle=(s*(s-a)*(s-b)*(s-c))**.5
print("area of triangle is",area_triangle)
