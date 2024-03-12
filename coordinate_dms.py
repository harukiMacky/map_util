class GridDMS:
    """緯度経度の60進法を表すクラス
    度、分、秒の情報を格納する。
    """

    def __init__(self, degree: int, minute: int, second: int) -> None:
        """コンストラクタ
        DDD°mm.ssを各変数に格納する。

        Parameters
        -----------
        degree : int
            度
        minute : int
            分
        second : int
            秒
        """
        self.degree = degree
        self.minute = minute
        self.second = second

    def convert_to_dmg(self) -> float:
        """緯度経度を10進数に変換する"""
        return self.degree + self.minute / 60 + self.second / 3600
