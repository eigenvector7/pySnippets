"""
Quick sort implementation in python. Not inplace - uses new arrays to copy the sub arrays
"""

def qsorter(uslist):
    if len(uslist) < 2:
        return uslist
    pivot = uslist[(len(uslist)//2)]
    left = []
    right = []
    center = []
    for i in uslist:
        if i > pivot:
            right.append(i)
        elif i < pivot:
            left.append(i)
        else:
            center.append(i)

    return qsorter(left)+center+qsorter(right)

