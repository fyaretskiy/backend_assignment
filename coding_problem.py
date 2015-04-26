

def find_consecutive_runs(alist):
    found = []
    for number in range(0, len(some_array)-3):
        if alist[number] + 1 == alist[number+1] and alist[number] + 2 == alist[number+2]:
            found.append(number)
        if alist[number] - 1 == alist[number+1] and alist[number] - 2 == alist[number+2]:
            found.append(number)
    if found:
        return found
    else:
        return None


