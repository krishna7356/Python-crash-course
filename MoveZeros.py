def moveZeroe(number):
    j = 0  
    for index in range(len(number)):
        if number[index] != 0:
            number[j] = number[index]
            j += 1
    while j < len(number):
        number[j] = 0
        j += 1

    return number
