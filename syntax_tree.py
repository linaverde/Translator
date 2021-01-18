class Elem:

    def __init__(self, value):
        self.value = value
        self.childrens = []

    def add_child(self, elem):
        self.childrens.append(elem)

    def change_value(self, new_value):
        self.value = new_value
