text = input("Enter a text: ")
freq = {}
for char in text.lower():
    if char.isalpha():
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
print("Character frequencies (excluding spaces and special characters):")
print(freq)