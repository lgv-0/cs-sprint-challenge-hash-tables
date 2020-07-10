# Your code here

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []

    for query in queries:
        for _file in files:
            if _file.__contains__(query):
                result.append(_file)

    return result

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
