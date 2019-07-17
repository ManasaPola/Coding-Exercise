''' Daily Coding problem #35
This problem was asked by Google.

Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].'''
def main():
    input = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
    left = 0
    curr = 0
    right = len(input) - 1
    map = {}
    map['R'] = 1
    map['G'] = 2
    map['B'] = 3
    while curr <= right:
        if map[input[curr]] == 1:
            input[left], input[curr] = input[curr], input[left]
            left += 1
            curr += 1
        elif map[input[curr]] == 2:
            curr += 1
        else:
            input[curr], input[right] = input[right], input[curr]
            right -= 1
    print(input)
    # map = {}
    # map['R'] = 1
    # map['G'] = 2
    # map['B'] = 3
    # for j in range(1, 4):
    #     for i in range(1, len(input)):
    #         if map[input[i]] == j:
    #             input[idx], input[i] = input[i], input[idx]
    #             idx += 1

    # for i in range(1, len(input)):
    #     if map[input[i]] == 2:
    #         input[idx], input[i] = input[i], input[idx]
    #         idx += 1
    # for i in range(1, len(input)):
    #     if map[input[i]] == 3:
    #         input[idx], input[i] = input[i], input[idx]
    #         idx += 1

if __name__ == "__main__":
    main()