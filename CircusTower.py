def main():

    def Tower(persons):
        ans = 1
        maxAns = 0
        persons = sorted(persons, key=lambda p: (p[1], p[0]))
        print(persons)
        for i in range(1, len(persons)):
            if persons[i][0] >= persons[i-1][0] and persons[i][1] >= persons[i-1][1]:
                ans += 1
            else:
                maxAns = max(maxAns, ans)
                ans = 0
        return max(ans, maxAns)

    persons = [(60, 100), (70, 150), (56, 90), (75, 190), (60, 95), (68, 110)]
    L = Tower(persons)
    print(L)

if __name__ == "__main__":
    main()