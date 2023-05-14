

# word_frequenct.py


import sys
filename = sys.argv[1]


freq = {}
filename = "Alice_in_Wonderland.txt"
for piece in open(filename).read().lower().split():
    # Only consider alphabetic characters within this piece
    word = ''.join(c for c in piece if c.isalpha())
    if word:                  # require at least one alphabetic character
        freq[word] = 1 + freq.get(word, 0)


max_word = ''
max_count = 0  


# (key, value) tuples represent (word, count)
for (w,c) in freq.items():   
    if c > max_count:
        max_word = w
        max_count = c


if __name__ == '__main__':
    print('The most frequent word is', max_word)
    print('Its number of occurrences is', max_count)


# Output:


"""
The most frequent word is the
Its number of occurrences is 1632
"""