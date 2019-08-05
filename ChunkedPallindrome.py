def main():

    str = "voabcvo"
    count = [0]

    def check(s):
        # print(s)
        i = 0
        if len(s) <= 1:
            if len(s) == 1:
                count[0] += 1
            return

        j = len(s) - 1
        while "".join(s[:i+1]) != "".join(s[j:]):
            i += 1
            j -= 1

        if "".join(s[:i+1]) == "".join(s[j:]) and i <= j:
            # print("".join(s[:i+1]) , "".join(s[j:]))
            count[0] += 2

        check(s[i+1:j])


    check(list(str))
    print(count[0])






if __name__ == "__main__":
    main()