# Uses python3
def edit_distance(s, t):
    """Calculate the minimum distance (Max alignment)."""
    m = len(s) + 1
    n = len(t) + 1
    distance_table = {}
    for i in range(m):
        distance_table[i, 0] = i
    for j in range(n):
        distance_table[0, j] = j
    for i in range(1, m):
        for j in range(1, n):
            if s[i - 1] == t[j - 1]:
                mismatch = 0
            else:
                mismatch = 1
            distance_table[i, j] = min(distance_table[i, j - 1] + 1, distance_table[i - 1, j] + 1, distance_table[i - 1, j - 1] + mismatch)
    return distance_table[i, j]



if __name__ == "__main__":
    print(edit_distance(input(), input()))
