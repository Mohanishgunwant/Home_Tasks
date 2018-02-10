from functools import reduce
list1=[[1,2,3],[5,8,9],[8,9,5,6],[3,7,4,9]]
for i in list1:
    reduce(lambda x,y:x+y,i)
print(list1)
