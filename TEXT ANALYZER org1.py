import random

print("==================")
print("   TEXT ANALYZER   ")
print("==================")

while True:
    sentence = input("Enter a sentence: \n> ")

    if sentence:
        break

    print("Please enter a sentence.")

characters = len(sentence)

print("Characters:", characters)

sentence = sentence.lower()

words = sentence.split()

word_count = {}
for word in words:
    if word in word_count:
         word_count[word]+= 1
    else:
        word_count[word] = 1

print("words:",len(words))

unique_words = set(words)

print("unique_words", len(unique_words))

most_common = max(word_count, key=word_count.get)

print("most common word:", most_common)

longest_word = max(words, key=len)

print("longest word:", longest_word)

lucky_word = random.choice(words)

print("lucky_word:", lucky_word)
