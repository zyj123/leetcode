l = list([x for x in range(20)])

print(l)

def b_search(l, target):
    """
    :param l:
    :param tagget:
    :return:int
    """
    start, end = 0, len(l)-1

    while start <= end:
        mid = (start+end)//2
        if l[mid] == target:
            return mid
        elif l[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return start+1

res = b_search(l, 6)
print(res)