word = input("Enter a word: ")
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0

for r in word:
    if r == 'a' or r == 'e' or r == 'i' or r == 'o' or r == 'u':
        count = count + 1

print(count)
