def sequence(T):
    n = len(T)
    d_p_max = s_p = k_p = -1
    d = 1
    s = k = T[0]
    for i in range(n-1):
        if T[i] < T[i+1]:
            k = i + 1
            d+= 1
        else:
            if d_p_max < d:
                d_p_max = d
                s_p = s
                k_p = k
            k = s = i + 1
            d = 1
    if d_p_max <= 2:
        return False
    
    s_d = k_d = d_d_max = -1
    d = 1
    s = k = T[0]
    i = 0
    while i + 1 < n:
        if i >= s_p and i <= k_p:
            s = k = i = k_p + 1
            d = 1

        if T[i] < T[i + 1]:
            k = i+1
            d += 1
        else:
            if d_d_max < d:
                d_d_max = d
                s_d = s
                k_d = k
            s = k = i + 1
            d = 1
        i += 1
    if d_d_max <= 2:
        return False
    if T[k_p] < T[s_d] or T[k_d] < T[s_p]:
        return True
    else:
        return False
    

T = [2,15,17,13,17,19,23,2,6,4,8,3,5,7,1,3,2]
print(sequence(T))