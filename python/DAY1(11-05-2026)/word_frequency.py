sentence = 'apple banana apple mango banana apple'


frequency = sentence.split();

dict = {}

for words in frequency:
    if words in dict:
        dict[words] += 1;
    else:
        dict[words] = 1;
print(dict)

