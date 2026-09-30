def hanoi_solver(n):
    total_moves = 2 ** n

    start = [num for num in range(n, 0, -1)]
    mid = []
    end = []

    result = f'{str(start)} {str(mid)} {str(end)}'

    for move in range(1, total_moves):
        if move % 3 == 1:
            if n % 2 == 1:
                move_disk(start, end)
            else:
                move_disk(start, mid)

        if move % 3 == 2:
            if n % 2 == 1:
                move_disk(start, mid)
            else:
                move_disk(start, end)

        if move % 3 == 0:
            move_disk(mid, end)

        result += f'\n{str(start)} {str(mid)} {str(end)}'
    
    return result

def move_disk(source, dest):
    if source and dest:
        if source[-1] < dest[-1]:
            dest.append(source.pop())
        else:
            source.append(dest.pop())
    elif not source:
        source.append(dest.pop())
    else:
        dest.append(source.pop())

