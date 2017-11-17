searched = "the"
given = "jok"
word = ""
for pos in range(0,len(searched)):
    word += chr((ord(searched[pos])-ord(given[pos]))%26+ord('A'))
print(word)