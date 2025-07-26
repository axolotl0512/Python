even_number = list(i for i in range(1,10) if i % 2 == 0)
print(even_number)

alphabet = ["a","b","c","d","e"]

vowel = [a for a in alphabet if a in "aeiou"]
print (vowel)

text = "I am not sleepy, my eyes are wide open"

text = [c+"A" for c in text if c.lower() not in "aeiou"]
print ("".join(text))