#LIST WITH INT AND FLOAT BOTH 
different=[1,2.2,3.4,5]
print(different)
print(len(different))

#ACCESS ELEMENT OF LIST USING INDEXING 
print(different[1])

#INSERT ELEMENT AT i INDEX 
num=[11,12,13,14,15]
num.insert(3,121)
print(num)
print(num[0])

#NEGATIVE INDEXING WILL GIVE LAST VALUE 
print(num[-1])
print("\n")

#THIS WILL JOIN LIST 
print("MIXTURE OF LISTS")
mixture=[num,different]
print(mixture)

 
# name="arun", "sharma","shrimadhopur" 
# comma is used to sperate whithout comma u can not seperate 
name="arun" "sharma","shrimadhopur"
print(name)
 
# list is mutable means we can change values of list 
List=[1,2,3,4]
List.append(12)  # APPEND IS USE FOR ADD ELEMENT IN THE LAST 
print(List)

#DELETE ELEMENT IN LIST USING POP
n=[11,12,13,14,15]
print(n)
n.pop();  #if you use pop without any index value then it will remove last value 
n.pop(2)  # remove value form 2 index 
print(n)

#DELETE SEVERAL ELEMENT IN ARRAY USING DEL
p=[21,22,23,24,25]
del p[2:]
print(p)
p.extend([121,0,123])
print(p)

#MINIMUM AND MAXIMUM IN LIST 
print(min(p))
print(max(p))

#SUM OF ALL ELEMENT IN THE LIST 
print(sum(p))

#SORT A LIST-1
p.sort()    #print(p.sort()) --> output=None 
print(p)

#SORT A LIST-2
print(sorted(p))


square=[]
for i in range(1,11):
    square.append(i**2)
print(square)


L=["egg", "fish","vegetables","milk","pens"]
 
item_to_find="milk"
found_at=None     
#IF WE DON'T HAVE VALUE THAN WE SHOULD SPECIFY NONE
# None is not defined to be 0 or any other value. In Python, None is an object and a first-class citizen
                        
for i in range(len(L)):
    if L[i]==item_to_find:
        found_at=i
        break

print("item found at {0} index ".format(found_at))
 
#ADDING TWO LISTS 
n1=[1,2,3,4]
n2=["arun ","sharma",'kidhar']
n=n1+n2
print(n)


#ACCESS SINGLE CHARACTHER 
list=['arun','sharma']
print(list[1][0])

##########
list=["arun sharma"]
print(type(list))

atuple=("orange")
print(type(atuple))

###########
l=['apple','grapes','banana']
l[1:1]='mango'
print(l)

#.join convert list into string 
list=['arun','sharma']
rsult='_'.join(list)
print(rsult)