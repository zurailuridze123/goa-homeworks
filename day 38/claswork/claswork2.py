def აეიოუ(text):
    return sum(1 for char in text if char in "ა ე ი ო უ")
text = "გამარჯობა"
print(აეიოუ(text)) 
