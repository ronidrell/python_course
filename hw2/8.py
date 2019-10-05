def get_partition(S):
    letters = list(set(S))
    answer = []

    i = 0
    while S != "":
        answer.append("")
        sub_letters = list(set(S[:S.rfind(S[0]) + 1]))
        begin = min([S.find(letter) for letter in sub_letters])
        end = max([S.rfind(letter) for letter in sub_letters])
        answer[i] += S[begin:end + 1]
        S = S[end + 1:]
        i += 1
    return answer



if __name__ == "__main__":
   print(get_partition("qbqbcbqcqdufugduhxjhklxj"))