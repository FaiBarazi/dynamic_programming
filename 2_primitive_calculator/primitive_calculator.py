# Uses python3
import sys

def sequencer(n):
    tracker = {}
    result = [0, 0]
    if n == 1:
        return (result[1])
    for i in range(2, n + 1):
        result.append(1 + result[i - 1])
        if i % 2 == 0:
            result[i] = min(result[i], (1 + result[i // 2]))
        if i % 3 == 0:
            result[i] = min(result[i], (1 + result[i // 3]))
        if result[i] in tracker:
            tracker[result[i]].append(i)
        else:
            tracker[result[i]] = [i]
    return result[n], tracker


def optimal_sequence(n):
    if n == 1:
        result = [1]
        return result
    x = n
    result = [n]
    operations, trakcer = sequencer(n)
    for i in range(operations - 1, 0, -1):
        for j in trakcer[i]:
            if j == x - 1 or j == x / 2 or j == x / 3:
                result.append(j)
                x = j
    result.append(1)
    return reversed(result)


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
