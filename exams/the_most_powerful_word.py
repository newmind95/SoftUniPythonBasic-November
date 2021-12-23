command = input()

powerful_word = 0
most_powerful_word = ''

while command != 'End of words':
    word = command
    current_powerful_word = 0

    for ch in word:
        current_powerful_word += ord(ch)

    if word[0].lower() in 'aeiouy':
        current_powerful_word *= len(word)
    else:
        current_powerful_word = int(current_powerful_word / len(word))

    if current_powerful_word > powerful_word:
        powerful_word = current_powerful_word
        most_powerful_word = word

    command = input()

print(f'The most powerful word is {most_powerful_word} - {powerful_word}')
