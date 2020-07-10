def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []

    counters = {}
    for array in arrays:
        for integer in array:
            alreadyDone = counters.get(integer)
            
            if alreadyDone == None:
                alreadyDone = 1
            else:
                alreadyDone += 1

            counters.__setitem__(integer, alreadyDone)

    for x in counters:
        if counters[x] == len(arrays):
            result.append(x)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
