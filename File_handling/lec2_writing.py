#WRITE 
# intro=open("z1.txt ",'w')
# intro.write("hello man")
#all the data from file will be delted when program will run and hello man will be printed in the file 

# names=['arun','kushal','varun']
# with open('z2.txt','w') as intro:
#     for name in names:
#         print(name,file=intro ,end=' ')

#APPEND
#IF WE WANT TO ADD NEW DATA IN THE PLACE OF REPLACING THEN WE USE APPEND
# intro=open("file",'a')
# intro.write(" how are u ")


# arun=[]
# with open("z1.txt",'r') as intro:
#     for name in intro:
#         name.append(arun)
# print(arun)
# for name in arun:
#     print(name)


#COPY DATA OF ONE FILE TO ANOTHER
# f=open("file",'r')
# f1=open('my.txt','w')

# for data in f:
#     f1.write(data)

#CREATING A NEW FILE AND WRITING IN IT 
# name=("arun","kushal")
# with open("z3.txt",'w') as name_file:
#     print("my name",file=name_file,end="")
#     name_file.write(" is arun sharma")

#WRITE DATA OTHER THAN STRING 
x=666
new=open("z1.txt",'a')
print(str(x),file=new)
