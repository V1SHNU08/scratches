file2 = (12,0,None,23 ,None,2,None,2,None,23,None)
print(file2)
file3 = list(file2)
for x in file3 :
    if x == None:
        file3.remove(None)
        file4 = tuple(file3)
print(file4)