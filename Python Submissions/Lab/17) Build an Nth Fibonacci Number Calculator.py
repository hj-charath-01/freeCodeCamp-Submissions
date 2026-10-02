def fibonacci(n: int) -> int:
    if n < 0:
        return f'n cannot be negative'

    if n < 2:
        return n

    sequence = [0, 1]
    for _ in range(2, n + 1):
        prev = sequence[-1]
        prev2 = sequence[-2]

        next = prev + prev2

        sequence.append(next)

    return sequence[n]
