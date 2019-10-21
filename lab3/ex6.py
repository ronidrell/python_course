def if_elif_else_block(score):
    if score == 1:
        return "Winner"
    elif score == -1:
        return "Loser"
    else:
        return "Tied"

def result(score):
    return (score == 1 and "winner") or (score == -1 and "Loser") or ("Tied")

print(if_elif_else_block(-1))
print(result(-1))
