import re
text = 'Search you name inside this namestring '

a = re.search('name', text)
# a = re.findall('name',text)

# print(a)
# print(a.span())
# print(a.start())
# print(a.end())
# print(a.group()) #it return what we are searching for if the pattern is not present then it will give the error


# HOW TO SOLVE THIS
obj = re.compile('name')
A = obj.search(text)  # this will search inside text
B = obj.findall(text)  # this fill find all the occurence and return list
C = obj.fullmatch(text)  # this will return output when whole string is present
D = obj.match(text)  # this dosen't care about what is coming in the end

print(A.group())
# print(A.string()) this return string that was passed :::: not working 
# print(C)



#SPLIT FUNCTION
# /s = white space is present 
# /S =white space is not present 

mystr='I completed my B.TECH from private unviersity'
res = re.split('\s',mystr)
print(res)


#SUB FUNCTION = replaces the matches with the given text 

res = re.sub('\s',' * ',mystr)
print(res)