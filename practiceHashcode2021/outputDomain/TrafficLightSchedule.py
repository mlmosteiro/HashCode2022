class TrafficLightSchedule:
    def __init__(self, streetName: str = "", time: int = 0):
        self.streetName = streetName
        self.time = time

    def __str__(self) -> str:
        return self.streetName + " " + self.time.__str__()
