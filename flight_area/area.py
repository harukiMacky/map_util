from geojson import Polygon, Feature
from geopy import Point


class Area:
    """
    フライトエリア内の一部を表すクラス。

    Attributes
    -----------
    name : str
        エリア名（エリアAなど）
    point_list : list[geopy.Point]
        エリア周囲のポイントのリスト
    maximum_altitude : int
        最高高度
    """

    def __init__(
        self, name: str, point_list: list[Point], maximum_altitude: int
    ) -> None:
        self.name = name
        self.point_list = self._convert_point_for_geojson(point_list)
        self.maximum_altitude = maximum_altitude

    def _convert_point_for_geojson(self, point_list: list[Point]) -> list:
        """
        ポイントをgeojsonように変換する。
        """
        converted_point_list = []
        for p in point_list:
            point_str = p.format_decimal()
            point_str = point_str.replace(" ", "").split(",")
            converted_point_list.append([float(point_str[1]), float(point_str[0])])

        return converted_point_list

    def make_area(self) -> Polygon:
        """
        Geojsonクラス作成
        """
        # 始点と終点を一致させる
        if self.point_list[0] != self.point_list[-1]:
            self.point_list.append(self.point_list[0])

        area_info = self.name + " : " + str(self.maximum_altitude) + " ft"

        return Feature(
            geometry=Polygon(coordinates=[self.point_list]),
            properties={"name": area_info},
        )
