def selection_sort(items):
    for i in range(0, len(items) - 1):
        smallest_index = i
        for j in range(i + 1, len(items)):
            if items[smallest_index] > items[j]:
                smallest_index = j
                

        if i != smallest_index:
            items[i], items[smallest_index] = items[smallest_index], items[i]

    return items
