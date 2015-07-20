def find(lst, i):
    """Find item i in the list lst.

    If the item is in the list, return it. Otherwise, return None.

    Use recursion to solve this.

    >>> find(["a", "b", "c"], "a")
    'a'

    >>> find(["a", "b", "c"], "c")
    'c'

    >>> find(["a", "b", "c"], "d")
    """
    if lst:
        if i in lst[0]:
            return i
        else:
            return find(lst[1:], i)
    else: 
        return None

if __name__=="__main__":
    lst = map(str, raw_input().strip().split(" "))
    i = raw_input()
    res = find(lst, i)
    print res
