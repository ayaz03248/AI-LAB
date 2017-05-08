x = [[0,0,0,0,0],
     [1,0,1,0,0],
     [0,0,0,0,0],
     [0,1,1,0,0],
     [1,0,1,1,0]]

u = int(input("Enter any number"))
u =u-1;
for z in range(0,5):
     p = x[u][z]
     if(p == 1):
            print(z+1, end=",");

