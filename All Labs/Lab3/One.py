x = [[1,0,0,0,0],[1,0,1,0,0],[0,0,0,0,0],[0,1,1,1,0],[1,0,1,1,0]]

y = int(input("Enter Vertex Number in between 1 and 5: "))
y = y-1
for z in range(0,5):
    r = x[y][z];
    if(r==1):
        print(z+1)
print("are Adjacent")
print("There is a loop on location:")
for i in range(0,5):
    o = x[i][i]
    if(o==1):
        print("(",i+1,",",i+1,")")
