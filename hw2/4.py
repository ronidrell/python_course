def get_most_frequent(words, k):

    unique_words = set(words)
    words_count = {}

    for word in unique_words:
        words_count[words.count(word)] = words_count.get(words.count(word), [])
        words_count[words.count(word)].append(word)

    answer = [words_count.get(x) for x in sorted(list(words_count.keys()), reverse = True)]

    return answer[:k]

if __name__ == "__main__":
    print(get_most_frequent(["hello", "world", "hello", "my", "dear", "world", "hello"], 2))
    
