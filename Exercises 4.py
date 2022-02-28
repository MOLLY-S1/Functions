def starts_with_A(word):
    if (word[0]) == 'A':
        return True
    else:
        return False




#main Routine
word = input("what is your word? ").title()
print(starts_with_A(word))
