text = input()
vowel_sum = 0

for character in range(len(text)):
    if text[character] == "a":
        vowel_sum += 1
    elif text[character] == "e":
        vowel_sum += 2
    elif text[character] == "i":
        vowel_sum += 3
    elif text[character] == "o":
        vowel_sum += 4
    elif text[character] == "u":
        vowel_sum += 5

print(vowel_sum)