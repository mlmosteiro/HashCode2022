from inputDomain.Street import Street

from typing import List


class CarPath:
    def __init__(self, streets: List[Street]):
        self.streets = streets

    def __repr__(self) -> str:
        return " - ".join(self.streets)
