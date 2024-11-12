def search(text , word):
    return "Word found" if word in text else "Word not found"
text = input()
word = input()
print(search(text , word))

