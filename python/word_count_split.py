from collections import Counter

string1 = input("Please enter any String : ")
words = []

word_list = string1.split()

word_count = Counter(word_list)

print(dict(word_count.most_common(3)))