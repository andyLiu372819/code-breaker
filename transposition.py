def solve(s):

    n = len(s)

    gap = 1

    while gap <= n // 2:
        lst = []
        index = 0
        while index < n:
            if index + gap <= n:
                lst.append(s[index:index + gap])
            else:
                lst.append(s[index:])
            index += gap

        k = len(lst)
        res = ''
        for i in range(gap):
            for j in range(k):
                if j == k - 1:
                    if i < len(lst[k-1]):
                        res += lst[j][i]
                else:
                    res += lst[j][i]

        print(res)
        gap += 1


solve("TUTTMOWSIHINOSMRNEPIEEUZLXSESZ")
