# list=['a','b','c']
# string=''
# for a in list:
#     string+=a+" "
# print(string)

#JOIN METHOD 
list=['a','b','c']
newstring=",".join(list)
print(newstring)
#JOIN MEHTOD DOES NOT REQUIRE LOOPS 

letters="abcdefghijklmnopqrstuvwxyz"
string="".join(letters)  # " " is nessacary. For joining we want something 
print(string)