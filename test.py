from oop_project import chatbook

user1 = chatbook()
# print(user1.name) #can not be accessed because it is private
# print(user1.__name) #can not be accesssed either
# print(user1._chatbook__name) #can be accessed in this particular way (object._class__attribute)



#getter and setter
# print(user1.get_name())
# user1.set_name("Agent X")
# print(user1.get_name())

print(user1.id)
 
# user2 = chatbook()
# print(user2.id)

# user3 = chatbook()
# print(user3.id)

# user4 = chatbook()
# print(user4.id)


#using static method directly from class rather than object
chatbook.set_id(100)
user2 = chatbook()
print(user2.id) #100

user3 = chatbook()
print(user3.id) #101