n = int(input())
dic = dict()

for i in range(n):
    x, y = input().split()
    dic[x] = y

# print(dic)
# dic = dict(zip(a, b))

# Taking Inputs till NULL
names = list()
try:
    while True:
        x = input().strip()
        if x != "":
            names.append(x)
        else:
            break
except EOFError:
    pass

for i in names:
    if i in dic:
        print(i + '=' + dic[i])
    else:
        print('Not found')