def main():
    def findTheWinner(andrea, maria,  s):
        if s == "Even":
            i = 0
        elif s == "Odd":
            i = 1
        andreaScore = 0
        mariaScore = 0
        while i < len(andrea):
            andreaScore += andrea[i] - maria[i]
            mariaScore += maria[i] - andrea[i]
            i += 2

        if andreaScore == mariaScore:
            return "Tie"

        return "Andrea" if andreaScore > mariaScore else "Maria"

    andrea = [4,5,7]
    maria = [3,5,6]
    s = "Even"
    ans = findTheWinner(andrea, maria, s)
    print(ans)



if __name__ == "__main__":
    main()