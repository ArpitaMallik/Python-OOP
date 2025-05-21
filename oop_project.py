class chatbook:
    def __init__(self):
        self.__name = 'Sam' # private attribute(encapsulated)
        self.email = ''
        self.password = ''
        self.loggedIn = False
        # self.menu()

    def menu(self):
        user_input = input("""Welcome to Chatbook! How would you like to proceed?
                           1. Press 1 to create a new account
                           2. Press 2 to login
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit \n""")
        
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
             self.mypost()
        elif user_input == '4':
            self.sendmsg()
        else:
            print("Exiting the program.")
            exit()
    
    def signup(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        self.email = email
        self.password = password
        print("Account created successfully!")
        print("\n")
        self.menu()

    def signin(self):
        if self.email == "" and self.password == "":
            print("Please sign up first!")
        else:
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            if self.email==email and self.password==password:
                print("Logged in successfully!")
                self.loggedIn = True
            else:
                print("Please enter the correct credentials")
        print("\n")
        self.menu()

    def mypost(self):
        if self.loggedIn == True:
            text = input("What's on your mind?")
            print(f"Following content has been posted: {text}")
        else:
            print("Sign in first to post something!")
        
        print("\n")
        self.menu()
    

    def sendmsg(self):
        if self.loggedIn == True:
            text = input("Enter your message: ")
            friend = input("Enter the name of your friend: ")
            print(f"Message sent to {friend}: {text}")
        else:
            print("Sign in first to send a message!")
        print("\n")
        self.menu()


obj = chatbook()