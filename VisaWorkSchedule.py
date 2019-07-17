
def main():
    def findSchedules(pattern, totalWorkHours, maxPerDay):
        workedHours = 0
        missingDays = []
        for i in range(len(pattern)):
            if 48 <= ord(pattern[i])-ord('a') <= 57:
                workedHours += int(pattern[i])
            else:
                missingDays.append(i)
        remainingHours = totalWorkHours - workedHours
        combos = set()
        def recurse(total, ans, remainingHours, workedHours, maxPer):
            if len(ans) == total:
                if sum(ans) == remainingHours:
                    combos.add(ans)


        ans = [0] * 2
        recurse(remainingHours, maxPerDay, 0, 0, ans)
        print(combos)

    pattern = "08??840"
    totalWorkHours = 24
    maxPerDay = 4
    s = findSchedules(pattern, totalWorkHours, maxPerDay)




if __name__ == "__main__":
    main()