class Character:
    """
    Class containing the info about the characters and methods to work with them.
    """
    def __init__(self, name: str, description: str, conversation=None):
        """
        Contains the following parameters:
        :param name: str
        :param description: str
        :param conversation: str / bool
        """
        self.name = name
        self.description = description
        self.conversation = conversation

    def __str__(self) -> str:
        """
        Prints the info about the class object
        :return: str
        """
        ans = self.name + " is here!"
        ans += "\n" + self.description
        return ans

    def set_conversation(self, conversation: str) -> None:
        """
        Updates the conversation parameter.
        :param conversation: str
        :return: None
        """
        self.conversation = conversation

    def talk(self) -> None:
        """
        Prints the speech with a character.
        :return: None
        """
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")


class Enemy(Character):
    """
    Child class for the character class to work with enemies.
    """
    enemies_defeated: int = 0
    # class variable

    def __init__(self, name: str, description: str):
        """
        Stores the following parameters:
        :param name: str
        :param description: str
        """
        super().__init__(name, description)
        self.weakness = None

    def __str__(self) -> str:
        """
        Prints the info about a class object.
        :return: str
        """
        return self.name + "is your enemy!"

    def fight(self, item: str) -> bool:
        """
        Method allowing to fight enemies with items.
        :param item: str
        :return: bool (True if the fight is won; False if lost)
        """
        if item == self.weakness:
            print("You fend " + self.name + " off with the " + item)
            Enemy.enemies_defeated += 1
            return True
        else:
            print(self.name + " crushes you, puny adventurer!")
            return False

    def set_weakness(self, weakness: str) -> None:
        """
        Updates the weakness of the enemy.
        :param weakness: str
        :return: None
        """
        self.weakness = weakness

    def get_weakness(self) -> str:
        """
        Gets the weakness parameter.
        :return: str
        """
        return self.weakness

    @staticmethod
    def get_defeated() -> int:
        """
        Static method to return the result of the fight.
        :return: str
        """
        return Enemy.enemies_defeated

    @staticmethod
    def set_defeated(number_defeated: int) -> None:
        """
        Updates the results of the fights and the number of victories.
        :param number_defeated: int
        :return: None
        """
        Enemy.enemies_defeated = number_defeated


class Friend(Character):
    """
    Child class for Character to work with friends objects.
    """
    def __init__(self, name: str, description: str):
        """
        Stores the following parameters:
        :param name: str
        :param description: str
        """
        super().__init__(name, description)

    def __str__(self) -> str:
        """
        Prints the info about the friend object.
        :return: str
        """
        return self.name + "is your friend!"
