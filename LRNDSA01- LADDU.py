# cook your dish here
for _ in range(int(input())) :
    N, country = input().split()
    min_laddus = 200 if country == "INDIAN" else 400
    laddus = 0
    for _ in range(int(N)) :
        info = input().split()
        if info[0] == "CONTEST_WON" :
            laddus += 300
            if int(info[1]) < 20 :
                laddus += 20- int(info[1])
        elif info[0] == "TOP_CONTRIBUTOR" :
            laddus += 300
        elif info[0] == "BUG_FOUND" :
            laddus += int(info[1])
        elif info[0] == "CONTEST_HOSTED" :
            laddus += 50
    print(laddus//min_laddus)