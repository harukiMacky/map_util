from dms import PointDMS


class LongitudeLatitudePoint:
    """緯度経度

    Attributes
    ----------
    x : float | int
        経度。東経を正の数とする。
    y : float | int
        緯度。北緯を正の数とする。
    """

    def __init__(self, x: float | PointDMS, y: float | PointDMS) -> None:
        """コンストラクタ
        DEGもしくはDNS形式の緯度・経度を設定する。
        """
        if type(x) == type(y):
            self.x = x
            self.y = y
        else:
            raise TypeError("座標はDEGもしくはDNS表記で統一してください。")
