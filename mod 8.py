def taskoutside(item_need, debuff, weapons, weaknesses ):
    for item in item_need:
        if item in weapons:
            print("You have all of the required items!")
        else:
            print("You do not have the required items.")
            return False

    for debuff in debuff:
        if debuff in weaknesses:
            print("You have all of the required items!")
        else:
            print("You do not have the required items.")
            return True


class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_nickname(self):
        return self.nickname

    def get_weapons(self):
        return self.weapons

    def get_debuff(self):
        return self.weaknesses

    def profile(self):
        return self.nickname, self.weapons, self.weaknesses

    def task1(self, item_need, debuff, ):
        for item in item_need:
            if item in self.weapons:
                print("You have all of the required items!")
            else:
                print("You do not have the required items.")
                return False

        for debuff in debuff:
            if debuff in self.weaknesses:
                print("You have all of the required items!")
            else:
                print("You do not have the required items.")
                return True

player1 = character('','','')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']

for item in player1.weapons:
    print("Item:", item)

for debuff in player1.weaknesses:
    print("Debuff:", debuff)

task1_s = ["Rope", "Coat", "First Aid Kit"]
task1_w = ["Slow"]

if player1.task1(task1_s, task1_w):
    print("Yes, you can go ahead and climb the mountain")
else:
    print("Sorry, but you are not able to climb!")

task2_s = ["Pan", "Groceries"]
task2_w = ["Small"]

# if player1.task1(task1_s, task1_w):
#     print("Yes, you can go ahead and climb the mountain")
# else:
#     print("Sorry, but you are not able to climb!")
#
# if taskoutside(task1_s, task1_w, player1.weapons, player1.weaknesses):
#     print("Yes, you can go ahead and climb the mountain")
# else:
#     print("Sorry, but you are not able to climb!")

if player1.task1(task2_s, task2_w):
    print("Yes, you can go ahead and cook!")
else:
    print("Sorry, but you are not able to cook!")
