

def solve(s):
    def get_beauty(substr):
        c={}
        # print("Checking Substring: ",substr)
        for i in substr:
            if i in c:
                c[i] += 1
            else:
                c[i] = 1
        counts = list(c.values())
        if not counts:
            return 0
        return max(counts) - min(counts)

    i = 0
    sb = 0
    while i < len(s):
        j = i
        while j <= len(s):
            b = get_beauty(s[i:j])
            # print(b)
            if b:
                # print("Added")
                sb += b
            j += 1
        i += 1
    return sb


s = "aabcbaa"

print(solve(s))