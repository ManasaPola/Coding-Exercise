"""This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2."""
def main():
    intervals = [(60, 75), (0, 50), (100, 150)]
    intervals = sorted(intervals, key=lambda x : x[1])
    timer = 0
    count = 0
    for i in intervals:
        if timer <= i[0]:
            timer = i[1]
            count += 1
    print(count)

if __name__ == "__main__":
    main()