#funtion to print a range of letters in Capatils
def print_word(word, number):
    word1 = word[0: number]
    word2 = word[number:len(word)]
    print(f"{word1.upper()}{word2}")





#main Routine
word_ = input("word: ")
number_ = int(input("number to be capitalised: "))
print_word(word_, number_)
