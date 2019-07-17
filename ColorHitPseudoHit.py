def main():
    colorMap = {'B':0, 'G': 1, 'R':2, 'Y': 3}

    def hits(code, guess):
        hitCount = 0
        pseudo_hit = 0
        color_guess = [0] * 4
        color_include = [0] * 4
        color_hit = [0] * 4
        for i in range(4):
            c = colorMap[code[i]]
            g = colorMap[guess[i]]
            if code[i] == guess[i]:
                hitCount += 1
                color_hit[c] = 1
            color_guess[g] = 1
            color_include[c] = 1

        for i in range(4):
            pseudo_hit += color_guess[i] and color_include[i] and not color_hit[i]

        return hitCount, pseudo_hit

    vals = hits("YYBB", "BBYY")
    print(vals)


if __name__ == "__main__":
    main()