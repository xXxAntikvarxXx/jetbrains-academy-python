# put your python code here
words = input().split(' ')
counter = {}
for word in words:
    word = word.lower()
    if word not in counter:
        counter[word] = 0
    counter[word] += 1

for word, count in counter.items():
    print(f"{word} {count}")
