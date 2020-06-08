# import sys
# sys.stdin = open('../input.txt', 'r')
# sys.stdout = open('../output.txt', 'w')

def solution(K, nums) :
    ans = 0
    for n in nums :
        if n > K :
            ans += n-K
    print(ans)

for _ in range(int(input())) :
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))

    solution(K, nums)