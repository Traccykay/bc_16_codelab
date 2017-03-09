def words(str):def words(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word.isdigit():
            if int(word) in counts:
                counts[int(word)] += 1
            else:
                counts[int(word)] = 1
        else:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1

    return counts
