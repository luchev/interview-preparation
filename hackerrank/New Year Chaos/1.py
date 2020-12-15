# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(1)

def minimumBribes(q):
    swaps = 0
    for index, value in enumerate(q):
        if index + 2 < value - 1:
            return 'Too chaotic'
        for i in range(max(0, value - 2), index):
            if q[i] > q[index]:
                swaps += 1
    return swaps

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
