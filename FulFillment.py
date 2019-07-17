import heapq
def main():
    numOfParts = 4
    parts = [8,6,4,12]

    def minimumTime(parts, ans):
        print(parts)
        if len(parts) == 1:
            return
        heap = parts
        heapq.heapify(heap)
        val1 = heapq.heappop(heap)
        val2 = heapq.heappop(heap)
        ans[0] = ans[0] + val1 + val2
        heapq.heappush(heap, val1 + val2)
        minimumTime(heap, ans)

    def minHelp(parts):
        if len(parts) == 1:
            return 0
        val1 = parts.pop(0)
        val2 = parts.pop(0)
        ans[0] = ans[0] + val1 + val2
        print(ans[0])
        parts.append(val1+val2)
        minHelp(parts)

    ans = [0]
    minHelp(parts)
    print(ans[0])

if __name__ == "__main__":
    main()