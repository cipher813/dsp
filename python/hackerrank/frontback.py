def front_back(s1, s2):
    h1 = len(s1)//2
    h2 = len(s2)//2
    if len(s1)%2 == 0:
        if len(s2)%2 == 0:
            return s1[:h1] + s2[:h2] + s1[h1:] +s2[h2:]
        else:
            return s1[:h1] + s2[:h2+1] + s1[h1:] +s2[h2:]
    else:
        if len(s2)%2 == 0:
            return s1[:h1+1] + s2[:h2] + s1[h1:] +s2[h2:]
        else:
            return s1[:h1+1] + s2[:h2+1] + s1[h1:] +s2[h2:]
