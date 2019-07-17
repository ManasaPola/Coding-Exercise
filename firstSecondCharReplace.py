def main():
    InputStr= "ABCAAACA"
    d = {}
    for i in range(len(InputStr)):
        if InputStr[i] in d:
            l = d.get(InputStr[i])
            l.append(i)
            d[InputStr[i]] = l
        else:
            d[InputStr[i]] = [i]
    n = 1
    lstring = list(InputStr)
    for key in d:
        if len(d[key]) >= 2 and n <= 2:
            l = d[key]
            for i in l:
                lstring[i] = str(n)
            n += 1
    print("".join(lstring))
    
if __name__ == "__main__":
    main()