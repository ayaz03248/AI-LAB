from math import sqrt
x = int(input('Enter a number'))
dic = {}
for i in range(1,x+1):
    dic[i] = sqrt(i)
print(dic)


