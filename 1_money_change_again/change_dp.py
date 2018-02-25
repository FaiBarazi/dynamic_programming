# Uses python3
import sys

def get_min_change(change):
    return min(change)

def get_change(money):
    """Return change matrix.

    param:
    money: int - money value
    coins: list - coins
    """
    coins = [1, 3, 4]
    change_matrix = [[0]]
    if money == 0:
        return 0
    for i in range(1, money + 1):
        row = []
        for j in range(len(coins)):
            if i >= coins[j]:
                row.append(get_min_change(change_matrix[i - coins[j]]) + 1)
        change_matrix.append(row)

    return get_min_change(change_matrix[-1])

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
