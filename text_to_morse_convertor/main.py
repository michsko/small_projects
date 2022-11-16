morse_alphabet = {"A" : ".-",  'B' : '-...',  'C' : '-.-.', 'D' : '-..', 'E' : '.',
                  'F' : '..-.', 'G' : '--.', 'H' : '....', 'I' : '..', 'J' : '.---',
                  'K' : '-.-', 'L' : '.-..', 'M' : '--', 'N' : '-.', 'O' : '---', 'P' : '.--.',
                  'Q' : '--.-', 'R' : '.-.', 'S' : '...', 'T' : '-', 'U' : '..-', 'V' : '...-',
                  'W' : '.--', 'X' : '-..-', 'Y' : '-.--', 'Z' : '--..',
                  ':' : '---...', ';' : '-.-.-.', '.' : '.-.-.-', '"' : '.-..-.', '1' : '.----',
                  '2' : '..---', '3' : '...--', '4' : '....-', '5' : '.....', '6' : '-....',
                  '7' : '--...', '8' : '---..', '9' : '----.', '0' : '-----', ' ': '... --- ...'}



converted_sentence = []
sentence = input("What do you wanna translate into morse code? :")
letters = list(sentence.upper())

for letter in letters:
    translated_letter = morse_alphabet[letter]
    converted_sentence.append(translated_letter)

print(converted_sentence)


