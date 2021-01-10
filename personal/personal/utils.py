def factorial(x: int) -> int:
    """Calculates factorial"""
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result