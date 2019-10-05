def get_partition(S):
    letters = list(set(S))
    answer = []

    i = 0
    while S != "":
        answer.append("")
        s = False
        sub_letters = set(S[:S.rfind(S[0]) + 1])
        while s == False:
            begin = min([S.find(letter) for letter in list(sub_letters)])
            end = max([S.rfind(letter) for letter in list(sub_letters)])
            answer[i] += S[begin:end + 1]
            S = S[end + 1:]
            if sub_letters == set(answer[i]):
                s = True
            else:
                sub_letters = set(answer[i])
        i += 1
    return answer



if __name__ == "__main__":
   print(get_partition("qbqbcbqcqdufugduhxjhklxj"))
