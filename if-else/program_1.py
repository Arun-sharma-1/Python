# age to enter in party is between 18 to 31
"""
name=input("Enter you name ")
age=int(input("what is ur age {} ".format(name )))
if 18<age<31:
    print("welcome")
else:
    print("come when u are above 18")
Level 1
1.
A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount.
2.
Take values of length and breadth of a rectangle from user and check if it is square or not.
3.
Take three int values from user and compare them.
4.
A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user.
5.
A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.
6.
Take input of age of 3 people by user and determine oldest and youngest among them.
7.
Write a program to print absolute vlaue of a number entered by user. E.g.-
INPUT: 1        OUTPUT: 1
INPUT: -1        OUTPUT: 1
8.
A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.
9.
Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.
 
# 1st PROGRAM 
name=input("Enter ur Name: ")
Salary=float(input("Enter ur salary: "))
print("How many years u had spend in our company")
yr=int(input())
if yr>=5:
    print("Congratulations!, u got 5% increment ")
    Salary= Salary+Salary/20
    print("ur net salary become {} :".format(Salary) )
else:
    print("work more hard to get increment ")
 

# 3rd PROGRAM
X,Y,Z= int(input("Enter value of x ")),int(input("Enter value of Y ")), int(input("Enter value of Z "))
if(X>Y and X>Z):
    print("X is greatest ")
elif(Y>Z and Y>X):
    print("Y is greatest ")
elif(Z>X):
    print("Z is greatest ")
else:
    print("all are equal ")
 
"""
#5th PROGRAM
 
X,Y,Z= int(input("Enter value of x ")),int(input("Enter value of Y ")), int(input("Enter value of Z "))
avg=(Z+Y+X)/3
if avg in range(91,101):
    print("A")
elif avg>=81 and avg<91:
    print('B')
elif avg>=71 and avg<81:
    print("C")
elif avg>51 and avg<61:
    print("D")
else:
    print("fail")
 

# 8th and 9th Program
n=int(input("Enter the no of classesd held: "))
attend=int(input("Enter the no of classes attend "))
x=1 # this is the bool 
per=(attend/n)*100
if per>=75:
    print("U can give the exam ")
elif per<75 and x==True:
    print("You can give the exam on basis of medical leave ")

else:
    print("U can not give the exam ")