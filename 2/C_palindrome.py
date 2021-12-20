s = input()

def changes_to_palindrome(s):
    i, j, = 0, len(s) - 1
    changes = 0
    while i < j:
        if s[i] != s[j]:
            changes += 1
        i += 1
        j -= 1
    return changes

if len(s) > 1:
    print(changes_to_palindrome(s))
else:
    print(0)