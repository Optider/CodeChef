from collections import Counter

def lapindrome(word) :
    mid = len(word)//2
    a = word[:mid]
    if len(word) & 1 :
        b = word[mid+1:]
    else :
        b = word[mid:]

    count = Counter(a)
    
    count_b = Counter(b)
    
    if count == count_b :
        return "YES"
    return "NO"

for _ in range(int(input())) :
    word = input()
    print(lapindrome(word))