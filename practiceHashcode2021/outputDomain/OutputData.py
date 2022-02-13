from outputDomain.TrafficLightSchedule import TrafficLightSchedule


class OutputData:

    def __init__(self, trafficLightsByIntersection = None):
         if trafficLightsByIntersection is None:
            self.trafficLightsByIntersection = {}

    def __str__(self) -> str:
        text = len(self.trafficLightsByIntersection).__str__()

        for intersectionId in self.trafficLightsByIntersection:
            text += "\n" + intersectionId.__str__()
            text += "\n" + len(self.trafficLightsByIntersection[intersectionId]).__str__() + "\n"
            text += "\n".join(map(str,self.trafficLightsByIntersection[intersectionId]))

        return text

    def addTrafficLightSchedule(self, intersectionId, trafficLightSchedule):
        if trafficLightSchedule.streetName == "":
            return

        if intersectionId not in self.trafficLightsByIntersection:
            self.trafficLightsByIntersection[intersectionId] = [
                trafficLightSchedule]
        else:
            self.trafficLightsByIntersection[intersectionId].append(
                trafficLightSchedule)
