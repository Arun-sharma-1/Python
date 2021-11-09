# IF SYNTAX
"""
if True:
    print("yes")

if False:
    print("nothing ")
    print("same indentaion")
print("this will work becz of different indentaion")
x=8
r=x%2
if r==0:
    print("even")
    if x>2: # this if will run if upper is true because of same indenatation
        print("greater")
        #look at the indenatation
        
else:
    print('odd')
 
"""
name=input("enter your name ")
age=int(input('What is your age,{0}?'.format(name))) 
print(age)

if age>18:
    print('u can vote ')
elif age==99:
    print("you died ")  # this elif will not work coz of if statement 
else:
    print(" u can't vote ")