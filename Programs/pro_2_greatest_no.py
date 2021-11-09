#Take three values from user and find the greatest one 
X,Y,Z= int(input("Enter value of x ")),int(input("Enter value of Y ")), int(input("Enter value of Z "))
if(X>Y and X>Z):
    print("X is greatest ")
elif(Y>Z and Y>X):
    print("Y is greatest ")
elif(Z>X):
    print("Z is greatest ")
else:
    print("all are equal ")
    

