with open('z3.txt','r') as intro:
    print(intro.tell()) #this tell the current posn of cursor by default it points to first char index
    print(intro.read(2))
    print(intro.read(3))
    print(intro.tell())
    intro.seek(7)#seek from the begining of the file 
    print(intro.tell())