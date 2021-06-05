text = input()

histogram = {}
for letter in text:
    histogram[letter] = histogram.get(letter, 0) + 1


for letter in sorted(histogram):
    print(F"{letter}: {histogram[letter]} time/s")

