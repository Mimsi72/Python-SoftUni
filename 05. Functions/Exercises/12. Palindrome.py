def palindrome(word, index):
    rev_idx = len(word) - index - 1
    if index >= rev_idx:
        return f"{word} is a palindrome"
    elif not word[index] == word[rev_idx]:
        return f"{word} is not a palindrome"
    return palindrome(word, index + 1)


print(palindrome("abcba", 0))