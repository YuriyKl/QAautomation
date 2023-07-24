#!/usr/bin/python3

multi_string = "Hello all. Here's pretty cold and hot. Choose yourself."
# print("counts", multi_string.count(".") )
sentences = multi_string.split(". ")

# solution 1
for sentence in sentences:
    print(sentence)

    i =0
    for word in sentence.split():
        # print(word)
        i += 1
    print(i)

# solution 2

print(f"words_number -> {[len(sentence.split(' ')) for sentence in multi_string.split('. ')]}")





















