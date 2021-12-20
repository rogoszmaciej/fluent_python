from math import hypot


class Vector:
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y}"

    def __abs__(self) -> int:
        return hypot(self.x, self.y)

    def __add__(self, vector: "Vector") -> None:
        self.x += vector.x
        self.y += vector.y

    def __bool__(self) -> bool:
        return bool(abs(self))

    def __mul__(self, scalar: int) -> "Vector":
        return Vector(self.x * scalar, self.y * scalar)
