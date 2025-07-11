sentence = input("Enter a sentence: ")
words = sentence.split()
unique_words = []
counts = []
for word in words:
    if word in unique_words:
        index = unique_words.index(word)
        counts[index] += 1
    else:
        unique_words.append(word)
        counts.append(1)
print("Word Frequencies:")
for i in range(len(unique_words)):
    print(f"{unique_words[i]}: {counts[i]}")