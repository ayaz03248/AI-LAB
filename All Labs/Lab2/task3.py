list = []
def sqr(x):
    ans = x*x
    return ans

for i in range(1,21):
    list.append(sqr(i))
    print(i," square is ",sqr(i))