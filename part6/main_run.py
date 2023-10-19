import pandas

def main():
#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
  data = pandas.read_csv("part6/Nato_phonetics_alphabet.csv")

  alphabet_dict = {row.letter:row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
  def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
      result = [alphabet_dict[letter] for letter in list(word)]
    except KeyError:
      print("Sorry, that word is not in the dictionary.")
      generate_phonetic()
    else:
      print(result)

  generate_phonetic()