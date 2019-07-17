import math
def main():
    def stock(input):
        map = {}
        for s in input:
            stock, val = s.split(':')
            if stock in map:
                l = map.get(stock)
                map[stock] = l.append(val)
            else:
                l = []
                l.append(val)
                map[stock] = l

    val = 1.399999
    vala = round(val, 2)
    val1 = '{:.2f}'.format(round(val, 2))
    print(float(val1))
    val2 = val // 0.01 / 100
    print((math.floor(vala * 100)) / 100.0)
    print(vala)
    ans = float('{0:.2f}'.format(val))
    ans1 = round(ans, 2)
    # ans = float(ans)
    print(ans1)
    print(type(ans))
    print('%.2f' % val)
    # format(a,'.2')
    orig_float = 1.3999#232569 / 16000.0
    short_float = float("{:.2f}".format(orig_float))


    arred = lambda x, n: x * (10 ** n) // 1 / (10 ** n)
    print(arred(3.9999999, 3)+0.001)













if __name__ == "__main__":
    main()