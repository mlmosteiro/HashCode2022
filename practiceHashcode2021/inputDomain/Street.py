class Street:
    def __init__(self, start: int, end: int, name:str, length: int):
        self.start = start
        self.end = end
        self.name = name
        self.length = length

    def __init__(self, args: list):
        self.start = args[0]
        self.end = args[1]
        self.name = args[2]
        self.length = args[3]

    def __repr__(self) -> str:
        return self.name + ": " + str(self.length) + " [" + str(self.start) + " - " + str(self.end) + "]"
