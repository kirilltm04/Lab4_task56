class Item:
    """
    Class with the item objects and methods to work with them.
    """
    def __init__(self, name: str, description=None):
        """
        Contains the following parameters:
        :param name: str
        :param description: str / bool
        """
        self.name = name
        self.description = description

    def __str__(self) -> str:
        """
        Prints the info about the Item class object.
        :return: str
        """
        return "The [" + self.name + "] is here - " + self.description

    def set_name(self, item_name: str) -> None:
        """
        Updates the name of the item.
        :param item_name: str
        :return: None
        """
        self.name = item_name

    def set_description(self, description: str) -> None:
        """
        Updates the description of the item.
        :param description: str
        :return: None
        """
        self.description = description

    def get_name(self) -> str:
        """
        Represents the name parameter.
        :return: str
        """
        return self.name

    def get_description(self) -> str:
        """
        Represents the description parameter.
        :return: str
        """
        return self.description
