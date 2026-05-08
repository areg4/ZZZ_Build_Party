def getRemovableIndices(str1, str2):
    n, m = len(str1), len(str2)
    
    if n != m + 1:
        return [-1]
    
    # prefix[i] = str1[0:i] == str2[0:i]
    prefix = [False] * (n + 1)
    prefix[0] = True
    
    for i in range(1, n):
        print(i)
        prefix[i] = prefix[i - 1] and (str1[i - 1] == str2[i - 1])

    print(prefix)
    
    # suffix[i] = str1[i:] == str2[i-1:]
    suffix = [False] * (n + 1)
    suffix[n] = True
    
    for i in range(n - 1, 0, -1):
        print(i)
        suffix[i] = suffix[i + 1] and (str1[i] == str2[i - 1])
    
    print(suffix)
    result = []
    
    for i in range(n):
        print(prefix[i] and suffix[i + 1])
        if prefix[i] and suffix[i + 1]:
            result.append(i)
    
    return result if result else [-1]

if __name__ == '__main__':
    str1 = "abdgggda"

    str2 = "abdggda"

    result = getRemovableIndices(str1, str2)

    print('\n'.join(map(str, result)))