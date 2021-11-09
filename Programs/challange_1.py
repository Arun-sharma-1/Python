
# select="-"
# while True:
#     if select==1:
#         print("I want to learn C")
        
#     elif select==2:
#         print("I want to learn cpp")

#     elif select==3:
#         print("I want to learn Python ")

#     elif select==4:
#         print("I want to learn Java")

#     elif select==0:
#         break
#     else:
#         print("1.c\n2.c++\n3.Python\n4.Java ")
#         print("Enter the key which course u want to take ")
         
#     select=int(input())


select="-"
while select!="0":
    if select in "1234":
        print("you have choosen {} key ".format(select))
     
    else:
        print("1.c\n2.c++\n3.Python\n4.Java ")
        print("Enter the key which course u want to take ")
         
    select= (input())

 