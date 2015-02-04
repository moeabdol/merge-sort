import numpy as np

# funciton to apply merge sort in O(n(log(n)))
def merge_sort(x):
    # if the list is of length one the return the single element list
    if len(x) == 1:
        return x

    # make sure you keep spliting the length till you end up with lists of
    # containing only a single number length one
    length = len(x) / 2
    a = merge_sort(x[:length])		# recursive call
    b = merge_sort(x[length:])		# recursive call

    # create list c which contains the sorted elements of both a and b
    c = []
    while len(a) > 0 and len(b) > 0:
        if a[0] <= b[0]:
            c.append(a.pop(0))
        elif a[0] > b[0]:
            c.append(b.pop(0))
        else:
            c.append(a.pop(0))
            c.append(b.pop(0))

    # make sure to append the left-overs
    if len(a) > 0:
        c.extend(a)
    elif len(b) > 0:
        c.extend(b)

    return c

if __name__ == '__main__':
    n = 20
    x = np.random.randint(low=1, high=10, size=(n,)).tolist()
    print 'Before\t', x
    x = merge_sort(x)
    print 'After\t', x
