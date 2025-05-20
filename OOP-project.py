class chatbook:
    def __init__(self):
        self.email = ''
        self.password = ''
        self.loggedIn = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to Chatbook! How would you like to proceed?
                           1. Press 1 to create a new account
                           2. Press 2 to login
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit""")
        
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            pass
        elif user_input == '4':
            pass
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
    

obj = chatbook()