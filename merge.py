def merge(a, b):

    if len(a) == 0:
        return b
    if len(b) == 0:
        return a

    if a[0] < b[0]:

        return [a[0]] + merge(a[1:], b)
    else:

        return [b[0]] + merge(a, b[1:])


if __name__ == "__main__":
    print(merge([1, 6, 7], [4, 5, 6]))
