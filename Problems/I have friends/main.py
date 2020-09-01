class User:
    def __init__(self, username):
        self.username = username
        self.friends = 0

    # fix this method
    def add_friends(self, n):
        self.friends += n
        print("{} now has {} friends.".format(
            self.username, self.friends
        ))
