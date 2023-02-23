import random
names = ["Peter", "Michell", "Jane", "Steve"]
places = ["Sofia", "Plovdiv", "Varna", "Burgas"]
verbs = ["eats", "holds", "sees", "plays with", "brings"]
nouns = ["stones", "cake", "apple", "laptop", "bikes"]
adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly"]
details = ["near the river", "at home", "in the park"]

print("Hello, this is your first random-generated sentence: ")

while True:
    random_name = random.choice(names)
    random_place = random.choice(places)
    random_verb = random.choice(verbs)
    random_noun = random.choice(nouns)
    random_adverb = random.choice(adverbs)
    random_detail = random.choice(details)

    print(f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noun} ")
    print("Click [Enter] to generate a new one.")

    input()