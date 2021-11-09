s1="my"
s2=" pyhton"
s3=" is not "
s4="to good"
print(s1+s2+s3+s4)

print(" my " " python " " is " " not " " to " "good " )

print("Arun "*10)
# print("Arun" *5+4) this is an error 
print("Arun "*(5+4))
print("Arun "*4+"4")

today="saturday"
print("to" in today ) # false 
print("sat" in today) # true
# print("sat" in saturday)  error
print("sat" in 'saturday') 
print("urday" in today)
#FIND INDEX OF A CHARACTHER 
str="ArunSharma"
print(str.index("S"))
# print(str.index('z')) -->error  

str="trying new things "
i=2
print(i, "we are " + str)