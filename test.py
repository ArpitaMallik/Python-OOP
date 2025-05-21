from oop_project import chatbook

user1 = chatbook()
# print(user1.name) #can not be accessed because it is private
# print(user1.__name) #can not be accesssed either
print(user1._chatbook__name) #can be accessed in this particular way (object._class__attribute)