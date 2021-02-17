import pandas

natoalphabetcsv = pandas.read_csv("nato_phonetic_alphabet.csv")

natoalphabet = {row.letter: row.code for (index, row) in natoalphabetcsv.iterrows()}

word = input("Type a word: ").upper()
convertedword = [natoalphabet[letter] for letter in word]

print(convertedword)
