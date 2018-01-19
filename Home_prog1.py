name_marks = {'Paul':56,'Eddy':78,'Anna':92,'Andrew':66,'Rahul':59,'Ben':88}
for k,v in name_marks.items():
    if v<60: 
        print("{:10} {:<10} failed".format(k,v))
    else:
        print("{:10} {:<10} passed".format(k,v))
