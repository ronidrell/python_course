def get_largest_perimeter(L):
    maxPer = 0
    for i in range(0, len(L) - 2):
        for j in range(i + 1, len(L) - 1):
            for k in range(j + 1, len(L)):
                if L[i] + L[j] > L[k] and L[i] + L[k] > L[j] and L[j] + L[k] > L[i]:
                    if L[i] + L[j] + L[k] > maxPer:
                        maxPer = L[i] + L[j] + L[k]
    if maxPer == 0:
        return "No such triangle"
    else:
        return maxPer

if __name__ == "__main__":
    print(get_largest_perimeter([
        12, 5, 3, 
        7, 1, 8
    ]))
