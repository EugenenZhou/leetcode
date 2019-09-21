def Lcstring(stringA,stringB):
    m = [[0 for i in range(len(stringB)+1)] for j in range(len(stringA)+1)]
    max = 0
    p = 0
    for i in range(len(stringA)):
        for j in range(len(stringB)):
            if stringA[i] == stringB[j]:
                m[i+1][j+1] = m[i][j] + 1
                if max < m[i+1][j+1]:
                    max = m[i+1][j+1]
                    p = i + 1
    return stringA[p-max:p],max
def Lcsubsequence(stringA,stringB):
    m = [[0 for i in range(len(stringB)+1)]for j in range(len(stringA)+1)]
    for i in range(len(stringA)):
        for j in range(len(stringB)):
            if stringA[i] == stringB[j]:
                m[i+1][j+1] = m[i][j] + 1
            else:
                m[i + 1][j + 1] = max(m[i+1][j],m[i][j+1])
    return m[len(stringA)][len(stringB)]


stringA = 'absgdbwehwiahjf'
stringB = 'sdhfeibwehedhdw'
print(Lcstring(stringA,stringB))
print(Lcsubsequence(stringA,stringB))