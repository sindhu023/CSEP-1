def anagram(s1, s2,):
    n = len(s1)
    m = len(s2)
    if n != m:
        return False
    dic1 = {}
    dic2 = {}
    for x in range(n):
        if dic1.get(s1[x]):
            dic1[s1[x]] += 1
        else:
            dic1[s1[x]] = 1
    for y in range(m):
        if dic2.get(s2[y]):
            dic2[s2[y]] += 1
        else:
            dic2[s2[y]] = 1
    count = True
    for x in dic1.keys():
        if dic2.get(x):
            if dic1[x] != dic2[x]:
                flag = False
                break
        else:
            flag = False
            break
    return count

s1 = input('Enter first string;')
s2 = input('Enter second string:')
print(anagram(s1,s2))
