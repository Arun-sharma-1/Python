a = int(input("Enter value of a "))
b = int(input("Enter value of b "))
c = int(input("Enter value of c "))

d = "A is greater " if a > b and a > c else "B is greater " if b>c and b > a else "c is greater "if c>a and c>b else "All are equal "
print(d)
