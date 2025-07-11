sentence = input("Enter a sentence: ")
vowels = {'a', 'e', 'i', 'o', 'u'}
used_vowels = set()
for char in sentence.lower():
    if char in vowels:
        used_vowels.add(char)
print("Unique vowels used:", used_vowels)