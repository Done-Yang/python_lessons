class User():
    count = 0
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

        User.count += 1

    def say_hello(self):
        print("hello! I am {}".format(self.name))
    def __str__(self):
        return "user: {}, email: {}, password: {}".format(self.name, self.email, self.password)

    @classmethod    # Decorator function
    def number_of_user(cls): # instance ==> self class ==> cls
        print("Total User: {}".format(cls.count))   # cls.count == User.count // class method call instance method or class

user1 = User('kim', 'kim@gmail.com', '1423')
user2 = User('lee', 'lee@gmail.com', '4123')
user3 = User('cee', 'cee@gmail.com', '2314')

user1.number_of_user()