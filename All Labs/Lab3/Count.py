l = [[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]
user = int(input("Enter Vertex Number in between 1 and 5: "))
user = user-1;
c=0;
for x in range(0,5):
    t = l[user][x]
    if(t == 1):
        c=c+1;
print("OutDegree:",c)