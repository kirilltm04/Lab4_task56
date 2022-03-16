class Character:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.conversation = None

    def __str__(self):
        ans = self.name + " is here!"
        ans += "\n" + self.description
        return ans

    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")


class Enemy(Character):
    enemies_defeated = 0

    def __init__(self, name, description):

        super().__init__(name, description)
        self.weakness = None

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item)
            Enemy.enemies_defeated += 1
            return True
        else:
            print(self.name + " crushes you, puny adventurer!")
            return False

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness

    @staticmethod
    def get_defeated():
        return Enemy.enemies_defeated

    @staticmethod
    def set_defeated(number_defeated):
        Enemy.enemies_defeated = number_defeated


class Friend(Character):

    def __init__(self, name, description):
        super().__init__(name, description)

    def __str__(self):
        return self.name + "is your friend!"
