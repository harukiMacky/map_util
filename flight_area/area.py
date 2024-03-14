from geojson import Polygon, FeatureCollection


class Area:
    """1フライトエリア
    フライトエリア内の一部を表すクラス。

    Attributes
    -----------
    name : str
        エリア名（エリアAなど）
    point_list : list
        エリア周囲のポイントのリスト
    maximum_altitude : int
        最高高度
    """

    def __init__(self, name: str, point_list: list, maximum_altitude: int) -> None:
        self.name = name
        self.point_list = point_list
        self.maximum_altitude = maximum_altitude

    def make_area(self) -> Polygon:
        """
        Geojsonクラス作成
        """
        area_info = self.name + " : " + self.maximum_altitude + " ft"

        return Polygon(coordinates=[self.point_list], properties={"name": area_info})
