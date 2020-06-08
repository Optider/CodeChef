import sys
try :
    sys.stdin = open('../input.txt', 'r')
except FileNotFoundError:
    pass

def solution(word) :
    ans = 0
    count = 0

    i = 0
    while i < len(word)-1 :
        if word[i] == 'x' and word[i+1] == 'y' :
            count += 1
            i += 2
        else :
            i += 1
    i = 0
    ans = max(ans, count)
    count = 0
    while i < len(word)-1 :
        if word[i] == 'y' and word[i+1] == 'x' :
            count += 1
            i += 2
        else :
            i += 1
    i = 0
    ans = max(ans, count)
    count = 0
    while i < len(word)-1 :
        if word[i] != word[i+1] :
            count += 1
            i += 2
        else :
            i += 1

    ans = max(ans, count)
    print(ans)
    
T = int(input())
while T :
    T -= 1
    word = input()

    solution(word)