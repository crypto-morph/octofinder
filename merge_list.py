words_file_path = "words.txt"
wordsmith_words_file_path = "words_alpha.txt"
words = set()
wordsmith_words = set()
merged_words = set()

with open(words_file_path) as f:
    words = set(f.read().splitlines())
with open(wordsmith_words_file_path) as f:
    wordsmith_words = set(f.read().splitlines())
    
merged_words = words.union(wordsmith_words)

sortedResults=sorted(merged_words)

with open('merged_words.txt','w') as f:
    f.writelines('\n'.join(sortedResults))