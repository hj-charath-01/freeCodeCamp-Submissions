def range_of_numbers(start_num, end_num):
    if end_num < start_num:
        return []
    
    numbers = range_of_numbers(start_num, end_num - 1)
    numbers.append(end_num)

    return numbers
    