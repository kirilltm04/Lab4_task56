class Room:

    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None

    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character

    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description

    def get_name(self):
        return self.name

    def set_name(self, room_name):
        self.name = room_name

    def get_item(self):
        return self.item

    def set_item(self, item_name):
        self.item = item_name

    def describe(self):
        print(self.description)

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        # print( self.name + " linked rooms: " + repr(self.linked_rooms))

    def get_details(self):
        print(self.name)
        print("--------------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self


class Character:

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print(self.name + " is here!")
        print(self.description)

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return False


class Enemy(Character):
    enemies_defeated = 0

    def __init__(self, char_name, char_description):

        super().__init__(char_name, char_description)
        self.weakness = None

        # Fight with an enemy

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

    def steal(self):
        print("You steal from " + self.name)
        # How will you decide what this character has to steal?


class Friend(Character):

    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.feeling = None

    def hug(self):
        print(self.name + " hugs you back!")


class Item:

    def __init__(self, item_name):
        self.name = item_name
        self.description = None

    def set_name(self, item_name):
        self.name = item_name

    def get_name(self):
        return self.name

    def set_description(self, item_description):
        self.description = item_description

    def get_description(self):
        return self.description

    def describe(self):
        print("The [" + self.name + "] is here - " + self.description)
