# READING FILE AND OPENING
# arun=open("z3.txt",'r')
# for list in arun:
#     print(list)
# print(arun.read())

# OPENING FILE WITH DIFFERNET METHOD
# with open("z3.txt",'r') as arun:
# print(arun.read())
#     for line in arun:
#      print(line)


# READING DATA
arun = open("z3.txt", 'r')
# print(arun.readline())      #give top line
# print(arun.readline())      #give 2nd line
# print(arun.readline())      #give 3ed line
# print(arun.readline(4))   #gives 4 characther in top line


# READING FILE WITH WHILE LOOP-1
# with open('z3.txt','r') as intro:
#     line=intro.readline()
#     while line:
#         print(line,end="")
#         line=intro.readline()

# CONVERTING FILE TO LIST WITHOUT  LOOP
# with open("z3.txt",'r') as intro:
#     lines=intro.readlines()
# print(lines )


# CONVERTING FILE TO LIST
# intro = open("z3.txt", 'r')
# liness = []
# for line in intro:
#     liness.append(line)
# print(liness)

# REVERSE ORDER OF LINES
# intro = open("z3.txt", 'r')
# lines = intro.readlines()
# for line in lines[::-1]:
#     print(line, end="")


# HOW TO PRINT SINGLE LINE THAT CONTAIN SPECIAL STRING(name it )
# for i in arun:
#     if "B.TECH" in i.upper():
#     # if "sharma" in i.lower():
#      print(i,end="")
# arun.close()
