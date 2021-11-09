# write a password guessing program that  okeep track of how many times the user has entered the password wrong. If it is more than 3 
# times , print("you have denied acces") and terminate the program . if the password is correct ,print you have succesfully 
# logged in and terminate the  program
n=0
x=int(input("Enter the password "))
if x==1234:
    print("you have succesfully logined ")
    break
     
else:
    x=int(input("Enter password again "))
    if(x==1234):
         print("you have entered correect password ")
        break

    else:
        x=int(input("wrong password,enter again "))
            if(x==1234):
             print("you have entered correect password ")
             break

            else:
                x=int(input("wrong password,enter again "))
            

            
        




    

