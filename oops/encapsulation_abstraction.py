class Product:

    #create variables here
    # __ is used to create python private variables
    def __init__(self) -> None:
        self.__productId=""
        self.__price=""
        self.__productName=""
        #self.__isbest=""

    def setproduct(self ,pid ,name,price):
        self.__productId=pid;
        self.__price=price
        self.__productName=name
    def show_product(self):
        print('Product Name: {}\nPrice: {} \nproduct id: {}\n'.format(self.__productName ,self.__price , self.__productId))

    def value_update(self, newprice):
        self.__price=newprice


tv=Product()
tv.setproduct('e101','ArunSharma',1000)
# tv.__price=1221  u can't change the value this line will not give any error but value will remain same 
tv.value_update(1200)

#access private object directly
print(tv._Product__price)
print(tv.__price)  #This will give error we can not access private 
# tv.show_product(); 


# classs code  #
#access specifiers
class employee:
    
    def __init__(self,n,s,a):
        self.name=n
        self.salary=s
        self.__age=a
    def disp(self):
        print("Name is:",self.name)
        print("Salary is:",self.salary)
        print("Age is:",self.__age)
e1=employee("ABC",20000,30)
e1.disp()

print(e1.name)
print(e1.salary)
#to access private member directly
print(e1._employee__age)

print(e1.__age)#will give error

