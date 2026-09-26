def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[-1]
    lesser = []
    sorted_equals = []
    greater = []

    for _ in array:
        if _ < pivot:
            lesser.append(_)
        elif _ > pivot:
            greater.append(_)
        else:
            sorted_equals.append(_)

    sorted_lesser = quick_sort(lesser)
    sorted_greater = quick_sort(greater)

    return sorted_lesser + sorted_equals + sorted_greater
