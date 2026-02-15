array = [1, 2, 2, 3, 4, 4, 4]


def num_unique(array):
    hashmap = {}

    for value in array:
        if value in hashmap:
            hashmap[value] += 1
        else:
            hashmap[value] = 1
    
    return len(hashmap)
print(num_unique(array))
