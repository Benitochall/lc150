#Is isomorphic
def isIsomorphic(s, t):
    a = zip(s,t)

    c = set(a)
    return len(c) == len(set(s)) == len(set(t))

print(isIsomorphic("egg","add"))