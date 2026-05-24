def palindromic(s, first, last):
    if first>=last:
        return True
    if s[first ] != s[last]:
        return False
    return palindromic(s, first+1, last-1)

s = "mwom"
first = 0
last = len(s)-1
print(palindromic(s, first, last))

    