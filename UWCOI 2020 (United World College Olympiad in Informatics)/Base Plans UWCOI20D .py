# United World College Olympiad in Informatics- A contest hosted by United World College of South East Asia - Dover Campus.

# Partially Accepted
# cook your dish here
for _ in range(int(input())) :
    N = int(input())
    field = []
    for i in range(N) :
        field.append(list(map(int, input())))
    print(N*(N+1)//2)