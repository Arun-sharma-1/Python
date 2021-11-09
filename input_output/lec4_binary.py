#OPEN A BINARY FILE 
with open("z4.txt",'bw') as bin_file:
    bin_file.write(bytes ( range(17) ) )

    #  for i in range(17):
    #      bin_file.write(bytes([i]))

#HOW TO SEE DATA OF BIANRY FILE 
with open("z4.txt",'br') as binfile:
    for b in binfile:
        print(b)


a=123
b=125
with open("z5.txt",'bw') as bin_file:
    bin_file.write(a.to_bytes(2,'big'))
    bin_file.write(b.to_bytes(2,'little'))

with open("z5.txt",'br') as bin_file:
    c=int.from_bytes(bin_file.read(2),"big");
    print(c)



# with open("pic.webp", 'br') as img:
#     with open('z.webp','bw') as image:
#      for i in img:
#         image.write(i)
 

 
    



