#METHODS TO FORM LIST 
# li=list("1234")  USING CONSTRUCTOR 
# print(li)
list_1=[]
list_2=list()
if list_1==list_2:
    print("Both are equal ")
else:
    print("Both are unequal ")

print(list("The both list are equal"))

############################
even=[2,4,6,8]
sorted_even=(even)
 
print(sorted_even is even)
sorted_even.sort(reverse=True)
print(even)

#ADDING LIST 
l1=[1,23,4,5,9]
l2=[12,14,16,18]
list=l1+l2
print(list)# --------|
                  #  ==>    these both are not same 
                  #  | 
list=[l1,l2]#---------
print(list)