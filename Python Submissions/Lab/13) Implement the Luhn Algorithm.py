def verify_card_number(card):
    numbers = []
    sum = 0

    for i in range(len(card) - 1, -1, -1):
        if card[i] == '-' or card[i] == ' ':
            continue
        numbers.append(int(card[i]))

    for i in range(len(numbers)):
        if i % 2 == 0:
            sum += numbers[i]
        else:
            double = numbers[i] * 2
            if double >= 10:
                double -= 9
            sum += double

    if sum % 10 == 0:
        return "VALID!"
    return "INVALID!"
