def python_fn():
    print("arun sharma")
    print("is here ")

# python_fn()
print(python_fn()) # this tells us output and what this function is returning 


def add(x,y):
    c=x+y;
    print(c)

print(add(1,2))

def add_sub_return(x,y):
    z=x+y
    s=x-y
    return z,s

# print(add_sub_return(2,2))
result1 ,result2=add_sub_return(2,2)
print(result1, result2)


#HOW TO GIVE SPACING IN TEXT 
def center_text(text):
    text=str(text)
    left_margin=(80-len(text)) // 2
    print(" "*left_margin , text)

center_text("arun sharma ")
center_text("how it is goint ")
center_text(12)
center_text("now i am watching money heist")
 
    
    