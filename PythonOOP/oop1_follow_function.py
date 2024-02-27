class User:
    count = 0
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

        User.count += 1

        self.follower = []
        self.following = []
    def __str__(self):
        return "user: {}, email: {}, password: {}".format(self.name, self.email, self.password)

    def follow(self, another_user):
        self.following.append(another_user)
        another_user.follower.append(self)

    def num_following(self):
        return len(self.following)

    def num_follower(self):
        return len(self.follower)

user1 = User("Young","young@codeit.kr","1423")
user2 = User("Yoonsoo","Yoonsoo@codeit.kr","1234")
user3 = User("leejonsuk","Leejonsuk@codeit.kr","4321")
user4 = User("Ani","Ani@codeit.kr","1243")

user1.follow(user3)
user1.follow(user4)
user2.follow(user3)
user3.follow(user1)
user4.follow(user3)
user4.follow(user2)

# print(user1, "follower: ", user1.num_follower(), "following: ", user1.num_following())
print(User.count)
print(user1.num_following())
