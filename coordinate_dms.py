class GridDMS:

    def __init__(self, degree: int, minute: int, second: int) -> None:
        self.degree = degree
        self.minute = minute
        self.second = second

    def convert_to_dmg(self) -> float:
        return self.degree + self.minute / 60 + self.second / 3600
