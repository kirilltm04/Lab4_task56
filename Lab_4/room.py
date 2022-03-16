class Room:
    """
    Class containing info about rooms and methods for the locations.
    """
    def __init__(self, room_name: str):
        """
        Stores the following parameters:
        :param room_name: str
        """
        self.name = room_name
        self.description = None
        self.linked_rooms = dict()
        self.character = None
        self.item = None

    def describe(self) -> str:
        """
        Describes the room.
        :return: str
        """
        print(self.description)

    def set_character(self, new_character: str) -> None:
        """
        Updates the info about the character.
        :param new_character: str
        :return: None
        """
        self.character = new_character

    def set_description(self, room_description: str) -> None:
        """
        Updates the info about the description of the room.
        :param room_description: str
        :return: None
        """
        self.description = room_description

    def set_name(self, room_name: str) -> None:
        """
        Updates the name of the room.
        :param room_name: str
        :return: None
        """
        self.name = room_name

    def set_item(self, item_name: str) -> None:
        """
        Updates the name of the item inside the room.
        :param item_name: str
        :return: None
        """
        self.item = item_name

    def get_name(self) -> str:
        """
        Returns the name of the room.
        :return: str
        """
        return self.name

    def get_character(self) -> str:
        """
        Returns the name of the character inside the room.
        :return: str
        """
        return self.character

    def get_description(self) -> str:
        """
        Returns the description of the character.
        :return: str
        """
        return self.description

    def get_item(self) -> str:
        """
        Returns the name of the item inside the room.
        :return: str
        """
        return self.item

    def link_room(self, room_to_link: str, direction: str) -> None:
        """
        Links the two neighbouring rooms.
        :param room_to_link: str
        :param direction: str
        :return: None
        """
        self.linked_rooms[direction] = room_to_link

    def __str__(self) -> str:
        """
        Describes the room and prints the results.
        :return: str
        """
        ans = self.name
        ans += "\n--------------------\n"
        ans += self.description + "\n"
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            ans += "The " + room.get_name() + " is " + direction + "\n"
        return ans[:-1]

    def move(self, direction: str) -> str:
        """
        Returns the direction of the player's move.
        :param direction: str
        :return: str
        """
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
