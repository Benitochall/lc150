
def findTheWinner(self, n, k):
    """
    :type n: int
    :type k: int
    :rtype: int
    """
    friends = [range(n)]
    start = 0
    while len(friends) >1:
        eliminated = friends[(k-1 + start) % len(friends)]
        index = friends.index(eliminated)
        friends.remove(eliminated)
        start = index
    return friends[0] +1