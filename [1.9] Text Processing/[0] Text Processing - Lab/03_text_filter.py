hidden_words = input().split(", ")
text = input()

for word in hidden_words:
    text = text.replace(word, "*" * len(word))

print(text)