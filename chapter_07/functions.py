def factorial(n):
    """returns n."""
    return 1 if n < 2 else n * factorial(n - 1)


def function_for_partial(a: str, b: str):
    return f"Param a: {a}, param b: {b}"


class CallableClass:
    value: int

    def __init__(self, value: int):
        self.value = value

    def __call__(self):
        return self.value
