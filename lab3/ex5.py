
'''words = ['pear', 'cabbage', 'apple', 'bananas']
print(min(words))  # => 'apple'
words.sort(key=lambda s: s[-1])  # Alternatively, key=operator.itemgetter(-1)
print(words)  # => ['cabbage', 'apple', 'pear', 'bananas'] ... Why 'cabbage' > 'apple'?
print(max(words, key=len))  # 'cabbage' ... Why not 'bananas'?
print(min(words, key=lambda s: s[1::2]))  # What will this value be?  (er, abg, pl, !!!aaa) '''


def alpha_score(upper_letters):
    """Return the alphanumeric sum of letters in a string, where A == 1 and Z == 26.

    The argument upper_letters must be composed entirely of capital letters.
    """
    return sum(map(lambda l: 1 + ord(l) - ord('A'), upper_letters))


def two_best(words):
    """Return the two words whose alphanumeric score of uppercase letters is the highest."""
    return sorted(
        words,
        key=lambda word: alpha_score(''.join(list(filter(lambda sym: sym.isupper(), word)))),
        reverse=True)[:2]


print(two_best(['hEllO', 'wOrLD', 'i', 'aM', 'PyThOn']))







