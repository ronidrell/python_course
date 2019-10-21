def number_of_matches(J, S):
    return len([letter for letter in S if letter in J])

if __name__ == "__main__":
    print(number_of_matches("Aa", "aAAbbbbb"))
    print(number_of_matches("z", "ZZ"))
    print(number_of_matches("Abc", "aAAbbbbb"))
    
