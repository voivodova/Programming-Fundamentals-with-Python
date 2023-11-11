morse_code_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z'
}

def morse_to_english(morse_code):
    words = morse_code.split(' | ')
    translated_words = []
    for word in words:
        letters = word.split(' ')
        translated_word = ''
        for letter in letters:
            if letter in morse_code_dict:
                translated_word += morse_code_dict[letter]
        translated_words.append(translated_word)
    return ' '.join(translated_words)

morse_code = input()
english_message = morse_to_english(morse_code)
print(english_message)
