def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """

    # Your code here
    if len(weights) < 2:
        return None
    
    for i in range(len(weights)):
        for x in range(len(weights)):
            if i is not x:
                if weights[i] + weights[x] == limit:
                    if i < x:
                        return (x, i)
                    else:
                        return (i, x)

    return None