x = [[1,0,0,0,0],
     [1,0,1,0,0],
     [0,0,0,0,0],
     [0,1,1,0,0],
     [1,0,1,1,0]]
y = int(input("Enter Node Number: "))
y = y-1
c=0
c1=0
for z in range(0,5):
    p = x[z][y]
    if(p==1):
        c=c+1
        print(z+1,end =",")
print("\nIndegree: ",c)
for z in range(0,5):
    r = x[y][z];
    if(r==1):
        c1 = c1+1
        print(z+1, end = ",")
print("\nOutdegree: ",c1)