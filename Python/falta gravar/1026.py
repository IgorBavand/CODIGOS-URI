while True:
    try:
        n, m = input().split()

        n = int(n)
        m = int(m)

        n = bin(n)[2:].zfill(32)
        m = bin(m)[2:].zfill(32)

        res = []
        for i in range(32):
            if n[i] != m[i]:
                res.append('1')
            else:
                res.append('0')

        res = ''.join(res)

        print(int(res, 2))





    except EOFError:
        break