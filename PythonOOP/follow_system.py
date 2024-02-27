class User:
    def __init__(self, username):
        self.username = username
        self.followers = set()
        self.following = set()

    def follow(self, user):
        self.following.add(user)
        user.followers.add(self)

    def unfollow(self, user):
        self.following.remove(user)
        user.followers.remove(self)

    def get_followers(self):
        return self.followers

    def get_following(self):
        return self.following

    @staticmethod
    def get_all_users():
        # This is just an example, you would typically load user data from a database or file
        users = []
        return users

users = User.get_all_users()
alice, bob, charlie, dave = users

alice.follow(bob)
bob.follow(charlie)
charlie.follow(dave)
charlie.follow(bob)

am_followers = bob.get_followers()
am_following = bob.get_following()

# Print the followers and following of Bob
print(f"Bob's followers: {am_followers}")
print(f"Bob is following: {am_following}")