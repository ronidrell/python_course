def count_unique_codes(words):
    morse_base = [
        ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
        "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
        "..-", "...-", ".--", "-..-", "-.--", "--.."
    ]

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    morse_dict = dict(zip(alphabet, morse_base))

    morse_words = {}

    for word in words:
        morse_word = ''
        for letter in word:
            morse_word += morse_dict[letter]
        morse_words[word] = morse_word

    return len(set(morse_words.values()))

if __name__ == "__main__":
    print(count_unique_codes(["gin", "zen", "gig", "msg"]))