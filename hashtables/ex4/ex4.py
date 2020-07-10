def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []

    for i in a:
        positive_i = i if i > -1 else i * -1
        if result.__contains__(positive_i):
            continue
        for x in a:
            if x == (i * -1):
                result.append(positive_i)
                break

    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
