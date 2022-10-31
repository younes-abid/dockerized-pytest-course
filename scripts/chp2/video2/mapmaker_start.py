
class Point():
    def __init__(self, name, lat, long) -> None:
        self.lat = lat
        self.long = long
    def get_lat_long(self):
        return self.lat, self.long


