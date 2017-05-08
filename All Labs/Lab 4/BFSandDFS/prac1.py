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
inp = int(input("Enter Node: "))
frontier.put(0)
explored = []
while True:
    if(frontier.empty()):
        print("Node not Found")
        break
    d = frontier.get()
    if(d in explored):
        continue
    explored.append(d)
    if(d==inp):
        print("Node ",inp," Found")
        break
    for y in range(0,9):
        if(x[d][y]==1):
            frontier.put(y)
print(explored)