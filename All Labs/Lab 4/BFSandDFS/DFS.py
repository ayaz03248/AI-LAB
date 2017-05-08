x = [[0,1,1,1,0,0,0,0,0],
     [0,0,0,0,1,1,0,0,0],
     [0,0,0,0,0,0,1,1,0],
     [0,0,0,0,0,0,0,1,1],
     [0,0,0,0,0,1,0,1,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0]]
i = 0
explored = []
target = int(input("Enter Node: "))
class depth():
    def DFS(i):
        explored.append(i)
        if(i == target):
            print("Node ",i," Found!")
            print(explored)
        if(i != target):
            for y in range(0,9):
                if(x[i][y]==1 and y not in explored):
                    depth.DFS(y)
depth.DFS(i)
if(target not in explored):
    print("Target Not Found!")