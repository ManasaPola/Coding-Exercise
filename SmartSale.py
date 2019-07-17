import collections
def main():
    def smartSale(ids, m):
        itemsCount = collections.Counter(ids)
        print(itemsCount)
        itemsCount = sorted(itemsCount.items(), key= lambda k: k[1])
        print(itemsCount)
        ans = 0
        if m == 0:
            return len(itemsCount)
        for item in itemsCount:
            if m < item[1]:
                return len(itemsCount) - ans
            else:
                m -= item[1]
                ans += 1
        return 0

    ids = [1,1,1,2,2,3]
    m = 2
    ans = smartSale(ids, m)
    print(ans)





if __name__ == "__main__":
    main()