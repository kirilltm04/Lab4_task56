class Item:

    def __init__(self, name):
        self.name = name
        self.description = None

    def __str__(self):
        return "The [" + self.name + "] is here - " + self.description

    def set_name(self, item_name):
        self.name = item_name

    def get_name(self):
        return self.name

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description
