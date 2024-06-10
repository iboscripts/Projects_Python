import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def alphabetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [new_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, Enter only letters")
        alphabetic()
    else:
        print(output_list)


alphabetic()


