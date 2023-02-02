text = input().lower()
words = ["sand", "water", "fish", "sun"]
print(sum([text.count(word) for word in words]))
