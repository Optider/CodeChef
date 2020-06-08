import sys
try :
    sys.stdin = open('../input.txt', 'r')
except FileNotFoundError :
    pass

coins_chef = {5:0, 10:0, 15:0}

def solution(customers) :
    global coins_chef
    for coin in coins_chef :
        coins_chef[coin] = 0

    # edge case
    if customers[0] != 5 :
        print("NO")
        return
    
    for c in customers :
        if c == 5 :
            coins_chef[5] += 1
        elif c == 10 :
            if coins_chef.get(5) :
                coins_chef[5] -= 1
                coins_chef[10] += 1
            else :
                print("NO")
                return
        elif c == 15 :
            if coins_chef.get(10) :
                coins_chef[10] -= 1
                coins_chef[15] += 1
            elif coins_chef.get(5) >= 2 :
                coins_chef[5] -= 2
                coins_chef[15] += 1
            else :
                print("NO")
                return

    print("YES")

T = int(input())
while T :
    T -= 1
    N = int(input())
    customers = list(map(int, input().split()))

    solution(customers)