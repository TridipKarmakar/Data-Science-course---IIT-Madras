words = ["moon","noon","dad", "dog", "cat", "madam"]
palindroms_numbers = []
for word in words :
    if word == word[::-1] :
        palindroms_numbers.append(word)
print(palindroms_numbers)
        