s = input("Enter the sentence : ")

words = s.split()
words.reverse()
result = " ".join(words)
print("Reversed sentence:", result)