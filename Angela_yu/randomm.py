# import random
# ans=random.randint(1,10)
# import random
# highest=10
# answer=random.randint(1,highest)
# print(answer)


import random
names=input('Enter names of your all friends ')
# Enter names of your all friends tarun,kushal,ravan, mangesh,rohit
pay_bill=names.split(',')
length=len(pay_bill)
a=random.randint(0,length-1)
print(pay_bill[a])
 

