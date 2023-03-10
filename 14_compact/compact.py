def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    copy = []
    for item in lst:
        if bool(item) == True:
            copy.append(item)
        else:
            continue
    return copy


print(compact([0, 1, 2, '', [], False, (), None, 'All done']))
