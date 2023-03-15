n=3
list=[]
for i in range(n):
    b=int(input())
    list.append(b)


months=["JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE","JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER"]
print(months[list[0]-1],list[1],","+str(list[2]))
