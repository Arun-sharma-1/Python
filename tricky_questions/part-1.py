"""
1.eval can be used as a variable.
2.Mathematical operations can not  be performed on a string  eg='123'
3.~x is equivalent to -(x+1).
4. ~ ~x = x
5.cmp(3, 1) cmp return true is x > y
6.round(-0.5) dependent on version -- > 0 
7.truncation division operator => //
8.The expression 1.7 % 2 is evaluated as 1.7 % 2.0 (that is, automatic conversion of int to float).
9. Format function returns a string.
10.s.__getitem__(3) = s[3]
11.len(s) = s.__len__()
12.To check whether string s1 contains another string s2, use s1.__contains__(s2)
13.i+j =  i.__add__(j)
""" 
number="1,2,3,4,5 "
print(number[1::3])

def x():
    pass
print(type(x)) #output--> <class 'function'>

l=[1,2,3]
print(l*2)

a=(100,)
print(a*2)  #(100, 100)

print(0.1 + 0.2 == 0.3) #output-->false
print(2+4.00, 2**4.0) #output-->6.0 16.0 coz result is automatically rounded off to one decimal place.
print(24//6 %3, 24//4//2) #1 3
print((ord('A'))) #ascii
print(chr(ord('A'))) #A
print(format("Welcome", "8"), end = '#') #7 length of charcther  than after space start ==>Welcome # (space come between in string)
print(format(111, "8"), end = '#') # space come in start 
# print(s.__getitem__(3)) if s is a string then this will give item at 4th posn s.getitem() is wrong syntax

'''
1. Which of the following expressions results in an error?
a) float(‘10’)
b) int(‘10’)
c) float(’10.8’)
d) int(’10.8’) #ans

2. The expression 2**2**3 is evaluates as: (2**2)**3.
a) True
b) False #right to left precedence

3.To find the decimal value of 1111, that is 15, we can use the function:
a) int(1111,10)
b) int(‘1111’,10)
c) int(1111,2)
d) int(‘1111’,2) #ans

4. The output of executing string.ascii_letters can also be achieved by:
a) string.ascii_lowercase_string.digits
b) string.ascii_lowercase+string.ascii_uppercase
c) string.letters
d) string.lowercase_string.uppercase

5.What will be the output of the following Python code?

print("abc DEF".capitalize())
a) abc def
b) ABC DEF
c) Abc def  #
d) Abc Def

''' 