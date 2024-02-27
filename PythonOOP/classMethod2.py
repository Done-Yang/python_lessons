class User():
    count = 0
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def from_list(cls, list_params):
        cls.name = list_params[0]
        cls.email = list_params[1]
        cls.password = list_params[2]

        return ("Name: {}, Email: {}, Password: {}".format(cls.name, cls.email, cls.password))

user1 = User.from_list(["young", "younghoon@codeit.kr", "123456"])
user2 = User.from_list(['yoon', 'yoonsoo@codeit.kr', 'abcdef'])

print(user1)
print(user2)