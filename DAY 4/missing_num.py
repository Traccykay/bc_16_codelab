def find_missing(a = [],b = []):
    
    a.sort()
    b.sort()

    if len(a) > len(b):
        for i in a:
            if i not in b:
                return i
            else:
                return 0

    elif len(b) > len(a):
        for i in b:
            if i not in a:
                return i
        else:
            return 0

    elif len(a)==len(b):
        return 0