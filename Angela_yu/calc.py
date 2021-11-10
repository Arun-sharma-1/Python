def calculator(first_no, next_no, op):
    if(op == '+'):
        return first_no + next_no
    if(op == '-'):
        return first_no - next_no
    if(op == '*'):
        return first_no * next_no
    if(op == '/'):
        return first_no / next_no
    
    
first_no = float(input("What is the first number "))
print('+', '- ', '/', '*')
flag =True
while flag:
    op = input('Choose any operation: ')
    next_no = float(input('What is the next no: '))
    res = calculator(first_no, next_no, op)
    print(f"{first_no} {op} {next_no} = {res} ")
    forward = input('Type y if u want to continue or otherwise type n ')

    if forward=='y':  
        first_no=res
    else:
        flag=False
 
    


     
 
