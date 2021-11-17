#Constructing class and initializing constructor

# class user:
#     def __init__(self) -> None:
#         print('new obj created ')

# user_1 = user()
# user_1.id = '100'
# user_1.name = 'arun'

# user_2= user()
# user_1.id='1'

# ------------------------

class user:
    def __init__(self ,name ,id) -> None:
        self.Name = name;
        self.Id = id
        self.followers =0
        self.following = 0

        # print(user.i)
    
    def Follow(self , user):
        self.followers+=1
        self.following+=1
      
user_1 = user('Arun', 1)
user_2 = user('Kushal',2)

user_1.Follow(user_2)
print(user_1.followers)
print(user_1.following)

# print(user_1)
# print(user_1.Name)
# print(user_1.Id)
# print(user_1.obj_created)
# user_1.object()
# print(user_1.obj_created)


