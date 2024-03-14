from dms import PointDMS


class LongitudeLatitudePoint:
    """緯度経度

    Attributes
    ----------
    latitude : float | int
        緯度。北緯を正の数とする。
    longitude : float | int
        経度。東経を正の数とする。
    """

    def __init__(self, latitude: float | PointDMS, longitude: float | PointDMS) -> None:
        """コンストラクタ
        DEGもしくはDNS形式の緯度・経度を設定する。
        """
        if type(latitude) == type(longitude):
            self.latitude = latitude
            self.longitude = longitude
        else:
            raise TypeError("座標はDEGもしくはDNS表記で統一してください。")
