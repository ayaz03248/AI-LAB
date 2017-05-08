import queue
x = [[0,1,1,1,1,0,0,0,0],
     [0,0,0,0,1,1,0,0,0],
     [0,0,0,0,0,1,1,0,0],
     [0,0,0,0,0,0,0,1,1],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0]]
frontier = queue.Queue()
frontier.put(0)
target = 9
explored = []
while(True):
    if(frontier.empty()):
        print("Target Does not Exist!")
        break
    d = frontier.get()
    if(d in explored):
        continue
    explored.append(d)
    if(d == target):
        print("Node: ",target," Found!!")
        break
    for y in range(0,9):
        p = x[d][y]
        if(p==1):
            frontier.put(y)
print(explored)

