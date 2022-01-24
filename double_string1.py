def double_string(data):
    catalogue = {i + j in data for j in data}
    counter = 0
    for word in data:
        if word in catalogue:
            counter +=1

    return counter

