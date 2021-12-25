#GENERATORS
#1. used to create sequences
#2. it will not create all object at single time time list and other data structures  

l =[x*x for x in range(1000000)] #this will take lot of time and may show overflow error

G= (x*x for x in range(100000000))
# while True:
#     print(next(G))


#GENERATING VALUES
def gen():
    yield 'A'
    yield 'B'
    yield 'C'

G= gen()
print(type(G))
# print(next(G))
try:
    while True:
        print(next(G))
except:
    pass