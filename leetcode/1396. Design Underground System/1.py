# Complexity (n = number of passengers)
# Time complexity: O(1) per operation
# Space complexity: O(n)

class UndergroundSystem:

    def __init__(self):
        self.enroute = {}
        self.journeys = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.enroute[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.enroute[id]
        del self.enroute[id]
        
        journey = (startStation, stationName)
        tripTime = t - startTime
        if journey not in self.journeys:
            self.journeys[journey] = (tripTime, 1)
        else:
            totalTime, nTrips = self.journeys[journey]
            self.journeys[journey] = (totalTime + tripTime, nTrips + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, nTrips = self.journeys[(startStation, endStation)]
        return totalTime / nTrips


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
