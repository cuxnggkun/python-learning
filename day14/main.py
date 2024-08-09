"""
1. open
2. process
3. close
"""
from pprint import pprint

# fo = open("data.txt", mode='w')

# data = []

# print(fo.read())
# for line in fo.readlines():
#     data.append(line.strip())
#
# print(data)

# for line in fo:
#     print(line.strip())

# print(fo.readline().strip())

# fo.write([])

# fo.close()

# with open("data.txt", mode='a') as fo:
#     fo.write("\nhello world")

ans = []

with open("iris.csv") as fo:
    header = fo.readline().strip().split(',')

    for line in fo:
        values = line.strip().split(',')
        iris_dict = dict(zip(header, values))
        ans.append(iris_dict)

pprint(ans)