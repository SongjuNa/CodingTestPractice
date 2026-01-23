word = input()

word_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

#cnt = []

for i in word_list:
    word = word.replace(i, '*')
print(len(word))