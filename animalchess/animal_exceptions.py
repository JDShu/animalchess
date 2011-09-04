class ReplaceException(Exception):
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def __str__(self):
        return "Tried to overwrite at " + repr(self.coordinates)

class NoPieceException(Exception):
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def __str__(self):
        return "No piece at " + repr(self.coordinates)
