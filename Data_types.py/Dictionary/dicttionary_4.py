d1 = {1: 'arun', 2: 'kusahl'}
d2 = {3: "ram", 4: 'ravan'}
d = {}
# for i in d1,d2: #only works with minm two dictionary
#     d.update(i)
# print(d)

d = d1.copy()
# d=d2.copy()

for key, value in d2.items():  # use for loop to iterate dict2 into the dict3 dictionary
    d[key] = value

print(d)

k = 'ram'  # key to search
keys = list(d.values())
print(keys)
for key in range(len(d)):
    if(k == keys[key]):
        print("yes")
        exit()
else:
    print('NO')
