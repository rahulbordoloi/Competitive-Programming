# https://codeforces.com/contest/1400/problem/B

def swords_axe(p, f, count_1, count_2, w_1, w_2): # Count_x -> Counts of Axes/Swords; w_x -> Weight of a(n) Axe/Sword
    
    count = 0
    cap_sum = p + f  # Capacity Sum

    if ((w_1 == w_2) & (count_1 == count_2)):
        if ((cap_sum // (2 * w_1)) >=  (2 * count_1)):
            count = 2 * count_2
        elif ((cap_sum // (2 * w_1)) < (2 * count_1)):
            count = cap_sum // count_1
    elif min(p, f) < w_2:
        count = count_1 if ((count_1 * w_1) > max(p, f)) else (max(p, f) // w_1)
        cap_sum -= count * w_1
    else:
        if (cap_sum // w_1) >= count_1:
            count = count_1
        else:
            count = cap_sum // w_1
        cap_sum -= (count * w_1)

        if (((cap_sum // w_2) >= count_2) & (((cap_sum // w_2) * count_2) >= cap_sum)):
            count += count_2
        else:
            count += cap_sum // w_2
            
    return count

# Main Method
if __name__ == '__main__':

    tc = int(input())
    ans = []

    while tc:
        p, f = map(int, input().split())
        cnts, cntw = map(int, input().split())
        s, w = map(int, input().split())

        flag = 0 if s < w else 1
        mod = 1000000007
        s, w = s % mod, w % mod

        if flag == 0:
            ans.append(swords_axe(p, f, cnts, cntw, s, w))

        elif flag == 1:
            ans.append(swords_axe(p, f, cntw, cnts, w, s))

        tc -= 1
    
    for i in ans:
        print(i, end = '\n')

    del mod, p, f, cnts, cntw, s, w, flag, ans
