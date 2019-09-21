def FirstNotRepeatingChar(s):
    dict1 = {}
    dict2 = {}
    length = 0
    for i in s:
        if i not in dict1 and i not in dict2:
            dict1[i] = length
        else:
            if i not in dict2:
                dict1.pop(i)
                dict2[i] = 1
        length += 1
    if not dict1:
        return -1
    for key in dict1:
        return dict1[key]
    # if not s:
    #     return -1
    # lis = list(filter(lambda c: s.count(c) == 1, s))
    # if not lis:
    #     return -1
    # return s.index(lis[0])




string = 'NXWtnzyoHoBhUJaPauJaAitLWNMlkKwDYbbigdMMaYfkVPhGZcrEwp'
res = FirstNotRepeatingChar(string)
print(res)