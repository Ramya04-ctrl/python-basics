text = input("Enter a string: ").lower() 
vowels = 0
consonants = 0

for ch in text:                           
    if ch >= 'a' and ch <= 'z':           
        if ch in ['a', 'e', 'i', 'o', 'u']:
            vowels += 1                 
        else:
            consonants += 1               

print("Vowels =", vowels)
print("Consonants =", consonants)
