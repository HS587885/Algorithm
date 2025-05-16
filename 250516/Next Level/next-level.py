user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class User:
    def __init__(self, id, level):
        self.id = id
        self.level = level

    def show(self):
        print(f"user {self.id} lv {self.level}")

user1 = User("codetree", 10)
user2 = User(user2_id, user2_level)

user1.show()
user2.show()




