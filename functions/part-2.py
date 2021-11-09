#MULTIPLE ARGUMENTS
# from typing import cast


def new(a, *b):
    print(a)
    print(b)
    c=0
    for i in b:
        c+=i;
    print(c+a)

x=new(3,1,21,1)

#MULTIPLE ARGUMENTS WITHOUT NAME
def mul_arg(local , **data):
    print(local)
    # print(data)

    for i,j in data.items():
        print(i,j)

mul_arg(10 , name='arun' , cast='brahmin',no='232323')

