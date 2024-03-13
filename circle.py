from geojson import Polygon, Point
import numpy
import json


class CircleZone:

    def __init__(self, radius: float, center: Point) -> None:
        self.radius = radius
        self.center = center

    def get_polygon(self, precision: float = 0.01) -> Polygon:
        theta = 0
        point_list = []
        while theta < 2 * numpy.pi:
            x = self.center["coordinates"][0] + self.radius * numpy.cos(theta)
            y = self.center["coordinates"][1] + self.radius * numpy.cos(theta)
            point_list.append([x, y])
            theta += precision  # これくらいで十分？

        return Polygon(coordinates=point_list)


circle = CircleZone(5, Point([0, 0]))
print(json.dumps(circle.get_polygon()))
