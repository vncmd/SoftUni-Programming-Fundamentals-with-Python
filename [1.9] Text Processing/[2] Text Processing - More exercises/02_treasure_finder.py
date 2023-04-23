secret_key = input().split()
encrypted = input()

keys_idx = 0
decrypted_text = ""
total_results = []

while encrypted != "find":
    result = ''

    for char in encrypted:
        if keys_idx >= len(secret_key):
            keys_idx = 0

        result += chr(ord(char) - int(secret_key[keys_idx]))
        keys_idx += 1

    total_results.append(result)
    result = ''
    keys_idx = 0

    encrypted = input()

for location in total_results:

    start_idx = location.index("&") + 1
    end_idx = location.index("&", start_idx + 1)

    start_coordinate, end_coordinate = location.index("<") + 1, location.index(">")

    print(f"Found {location[start_idx:end_idx]} at {location[start_coordinate:end_coordinate]}")
