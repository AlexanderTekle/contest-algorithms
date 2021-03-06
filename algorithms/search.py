
def bisect_left(func, val, low, high):
    """
    Like bisect.bisect_left, but works on functions.

    Return the index where to insert item x in list a, assuming a is sorted.

    The return value i is such that all e in a[:i] have e < x, and all e in a[i:] have e >= x.  So if x already appears
    in the list, a.insert(x) will insert just before the leftmost x already there.  Optional args lo (default 0) and hi
    (default len(a)) bound the slice of a to be searched.

    >>> bisect_left([1,2,3,3,4].__getitem__, 3, 0, 4)
    2
    >>> bisect_left([1,2,3,3,4].__getitem__, 4, 0, 4)
    4
    >>> bisect_left([1,2,3,6,8].__getitem__, 4, 0, 4)
    3
    """

    a = low
    b = high
    while b > a:
        guess = (a+b)//2

        if val > func(guess):
            a = guess+1
        else:
            b = guess

    return a

def bisect_right(func, val, low, high):
    """
    Like bisect.bisect_right, but works on functions.

    Return the index where to insert item x in list a, assuming a is sorted.

    low: the minimum possible value
    high: the maximum possible value + 1

    The return value i is such that all e in a[:i] have e <= x, and all e in a[i:] have e > x.  So if x already appears
    in the list, a.insert(x) will insert just after the rightmost x already there.

    >>> bisect_right([1,2,3,3,4].__getitem__, val=3, low=0, high=5)
    4
    >>> bisect_right([1,2,3,3,4].__getitem__, val=4, low=0, high=5)
    5
    >>> bisect_right([1,2,3,3,4].__getitem__, val=4, low=0, high=4)
    4
    >>> bisect_left([1,2,3,6,8].__getitem__, val=4, low=0, high=5)
    3
    >>> bisect_left([1,2,3,6,8].__getitem__, val=0, low=0, high=5)
    0

    When searching for 3, the following will be returned:
    [1,2,3,3,*4*]
    [1,2,*4*,5]
    [1,2,2,*]

    """
    a = low
    b = high
    while b > a:
        guess = (a+b)//2

        if val >= func(guess):
            a = guess+1
        else:
            b = guess

    return a

def find_peak(func, low, high):
    """
    Find a peak of a discrete function. The function input and output must be integers.
    min: optional minimum value - may speed up the search

    >>> find_peak([1,2,3,2,1].__getitem__, 0, 4)
    2
    >>> find_peak([1,2,3,4,5].__getitem__, 0, 4)
    4
    >>> find_peak([5,4,3,2,1].__getitem__, 0, 4)
    0
    >>> find_peak([1,2,3,3,3,4,3,3,3,3,2,1].__getitem__, 0, 11)
    5
    """
    def derivative(x):
        return func(x)-func(x+1)

    a = bisect_left(derivative, 0, low, high)

    result = func(a)
    index = a

    # Unfortunately the above only finds a value where there is no change, so we have to continue searching for the
    # maximum value. The binary search brings us close enough that this isn't an issue for most functions.

    # Search forward
    k = a
    while k <= high:
        d2 = func(k)
        if d2 < result:
            break
        else:
            result = d2
            index = k
            k += 1

    # Search backward
    k = a
    while k >= low:
        d2 = func(k)
        if d2 < result:
            break
        else:
            result = d2
            index = k
            k -= 1

    return index
