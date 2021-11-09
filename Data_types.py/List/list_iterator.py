from typing import Iterator


list=["Monday",r"Tuesday ","Wednesday","Thrusday ","Friday","Saturday","Sunday"]
Iterator=iter(list)
for day in range(0,len(list)):
    next_ele=(next(Iterator))
    print(next_ele)