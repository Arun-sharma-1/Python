"""
print('hello ' + input('Enter ur name: '));
print("Arun sharma have ") # correct syntax 
#   print("hello ") -->indenation error
# indentaion error occur when i give spaces in front of print statement 
#  we have to organise the program befor running 
apple=5
if apple==5:
 print("we have 5 apples ")
#  without give space in print line it is IndentationError we have to organise 
if apple==5:
    print("what he will do ")
#-->single line comment
# multi line comment        

x=4
y=5
z=x+y
print(z)
a=4//3;
print(a) # it will print only 1 coz we are using // 
print('hello world ')
# 8-9+  it is an error forget after +
print(2**3) # this is used for finding power of a number 
 
print('arun sharma')
print("arun sharma")
#  error --> print("arun "sharma"") 
#  error --> print('arun's laptop')  THESE ERROR CAN BE SOLVED
print("arun's laptop")
print('arun "sharma" \n' * 10) # operations on string 
print("arun"+"arun")
# \n is use for new line 
print( "why we are using\navin's diagram")
print( "why we are using\\navin's diagram")
print(r"why we are using\navin's diagram")

p=("a" ) * 3
q=("a" ) *2
print(p)
"""
print("\"arun \" sharma") 
print(""" ARUN "sharma" """)
name="""
       by the help of 3 
       double quotes lines
       break as it is. 
       space also became same 
 """
print(name)

convert="""
       by the help of 3\
       double quotes lines\
       break as it is.\
       space also became same 
 """
 
print(convert)
print("print can also\
convert line into different\
")   

a=12
b=4
c=a/b
print(type(c))
print(c)

letter="Arun_sharma"
backward=letter[10:0:-1]
print(backward)
backward=letter[10:-12:-1]
print(backward)
backward=letter[10::-1]
print(backward)
backward=letter[::-1]
print(backward)

letters="abcdefghijklmnopqrstuvwxyz"
back=letters[16:13:-1]
print(back)
back=letters[4::-1]
print(back)

#ASSIGNING VALUES 
a=b=c=d=12
print(b)

# a=b=1
a,b=11,12
print(a,b)

#Printing with %d
data=10
print("%d"%(data))

#d and f in printing statement
print('boys in class:%d'%(101))
print('boys in class:%0.2f'%(101))
print('boys in class :%5.2f ' %(5.333) )


