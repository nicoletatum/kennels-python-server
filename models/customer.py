class Customer():

    # Class initializer. It has custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, address, animal_id):
        self.id = id
        self.name = name
        self.address = address
        self.animal_id = animal_id