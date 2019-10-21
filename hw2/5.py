def is_valid(braces_string):
    braces = ""
    for x in braces_string:
        if x == "(":
            braces += "("
        if x == ")":
            braces = braces[:-1]
    if braces == "":
        return True
    else:
        return False


if __name__ == "__main__":
    print(is_valid("(()())"))
    
