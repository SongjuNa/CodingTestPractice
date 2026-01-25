words = [input() for _ in range(5)]
    
text = ""    
for i in range(15):
    for j in range(5):
        if i < len(words[j]):
            text += words[j][i]
print(text)