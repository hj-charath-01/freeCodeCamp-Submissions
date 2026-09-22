def square_root_bisection(number, tolerance = 0.01, max_iterations = 10):
    if number < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')

    if number == 0 or number == 1:
        print(f'The square root of {number} is {number}')
        return number

    square_target = number
    root = 0
    low = 0
    high = number if number > 1 else 1
    maximum = max_iterations

    while max_iterations:
        mid = (high + low) / 2

        root = mid
        if mid ** 2 < number:
            low = mid
        elif mid ** 2 > number:
            high = mid
        else:
            print(f'The square root of {square_target} is approximately {root}')
            return root

        max_iterations -= 1
        if 0 < (high - low) <= tolerance:
            print(f'The square root of {square_target} is approximately {root}')
            return root

    print(f'Failed to converge within {maximum} iterations')
    return None

