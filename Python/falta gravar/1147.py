while True:
    ps = input()
    if ps == '0': break
    p1 = input()
    p2 = input()
    p3 = input()
    p4 = input()
    p5 = input()
    p6 = input()
    p7 = input()
    p8 = input()

    #CAVALO

    ps = ps.replace('a','1')
    ps = ps.replace('b','2')
    ps = ps.replace('c','3')
    ps = ps.replace('d','4')
    ps = ps.replace('e','5')
    ps = ps.replace('f','6')
    ps = ps.replace('g','7')
    ps = ps.replace('h','8')

    #PEAO 1
    p1 = p1.replace('a','1')
    p1 = p1.replace('b','2')
    p1 = p1.replace('c','3')
    p1 = p1.replace('d','4')
    p1 = p1.replace('e','5')
    p1 = p1.replace('f','6')
    p1 = p1.replace('g','7')
    p1 = p1.replace('h','8')

    #PEAO 2
    p2 = p2.replace('a','1')
    p2 = p2.replace('b','2')
    p2 = p2.replace('c','3')
    p2 = p2.replace('d','4')
    p2 = p2.replace('e','5')
    p2 = p2.replace('f','6')
    p2 = p2.replace('g','7')
    p2 = p2.replace('h','8')

    p3 = p3.replace('a','1')
    p3 = p3.replace('b','2')
    p3 = p3.replace('c','3')
    p3 = p3.replace('d','4')
    p3 = p3.replace('e','5')
    p3 = p3.replace('f','6')
    p3 = p3.replace('g','7')
    p3 = p3.replace('h','8')

    p4 = p4.replace('a','1')
    p4 = p4.replace('b','2')
    p4 = p4.replace('c','3')
    p4 = p4.replace('d','4')
    p4 = p4.replace('e','5')
    p4 = p4.replace('f','6')
    p4 = p4.replace('g','7')
    p4 = p4.replace('h','8')

    p5 = p5.replace('a','1')
    p5 = p5.replace('b','2')
    p5 = p5.replace('c','3')
    p5 = p5.replace('d','4')
    p5 = p5.replace('e','5')
    p5 = p5.replace('f','6')
    p5 = p5.replace('g','7')
    p5 = p5.replace('h','8')

    p5 = p5.replace('a','1')
    p5 = p5.replace('b','2')
    p5 = p5.replace('c','3')
    p5 = p5.replace('d','4')
    p5 = p5.replace('e','5')
    p5 = p5.replace('f','6')
    p5 = p5.replace('g','7')
    p5 = p5.replace('h','8')

    p6 = p6.replace('a','1')
    p6 = p6.replace('b','2')
    p6 = p6.replace('c','3')
    p6 = p6.replace('d','4')
    p6 = p6.replace('e','5')
    p6 = p6.replace('f','6')
    p6 = p6.replace('g','7')
    p6 = p6.replace('h','8')

    p7 = p7.replace('a','1')
    p7 = p7.replace('b','2')
    p7 = p7.replace('c','3')
    p7 = p7.replace('d','4')
    p7 = p7.replace('e','5')
    p7 = p7.replace('f','6')
    p7 = p7.replace('g','7')
    p7 = p7.replace('h','8')

    p8 = p8.replace('a','1')
    p8 = p8.replace('b','2')
    p8 = p8.replace('c','3')
    p8 = p8.replace('d','4')
    p8 = p8.replace('e','5')
    p8 = p8.replace('f','6')
    p8 = p8.replace('g','7')
    p8 = p8.replace('h','8')

    linhas = []
    colunas = []

    if int(ps[0]) > 2 and int(ps[1]) > 2 and int(ps[0]) < 7 and int(ps[1]) < 7:
        linhas.append(int(ps[0]) + 2)
        colunas.append(int(ps[1]) + 1)

        linhas.append(int(ps[0])+ 2)
        colunas.append(int(ps[1]) - 1)

        linhas.append(int(ps[0]) + 1)
        colunas.append(int(ps[1]) + 2)

        linhas.append(int(ps[0]) + 1)
        colunas.append(int(ps[1]) - 2)

        linhas.append(int(ps[0]) - 2)
        colunas.append(int(ps[1]) + 1)

        linhas.append(int(ps[0]) - 2)
        colunas.append(int(ps[1]) - 1)

        linhas.append(int(ps[0]) - 1)
        colunas.append(int(ps[1]) - 2)

        linhas.append(int(ps[0]) - 1)
        colunas.append(int(ps[1]) + 2)


    elif int(ps[1]) <= 2:
        if ps[0] <= 2:







