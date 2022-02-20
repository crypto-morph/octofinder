################################
# Octofinder - by crypto-morph #
################################

import sys, yaml

## Module with Auto Octo Finder Utilities ##

# some handy subroutines
import utils

def split(word):
  return [char for char in word]

def check(word):
  return (len(word) != 8) or (word == "") or (not word.isalpha())

def findDifference(start,target):
  result = abs(start-target)
  return (result)
  
def calculateWords(start, words, maxTurns):
  results = dict()
  for target in words:
    target = target.upper()
    totalmoves = 0
    score = 0
    for i in range(8):
      lValue = ord(target[i])
      rValue = ord(start[i])
      moves = findDifference(lValue,rValue)
      totalmoves += moves
      score += ord(target[i]) - 65
    if totalmoves <= maxTurns:
      results[target] = [int(totalmoves),int(score)]
  return results

#Init
words_file_path = str()
wordsmith_words_file_path = str()
words = set()
wordsmith_words = set()

# Load config YAML for discord bot key and file with words list
stream = open('bot_config.yml','r')
config = yaml.safe_load(stream)

words_file_path = config['words_file_path']
wordsmith_words_file_path = config['wordsmith_words_file_path']
        

with open(words_file_path) as f:
    words = set(f.read().splitlines())
with open(wordsmith_words_file_path) as f:
    wordsmith_words = set(f.read().splitlines())


traits = str()
traits = input("Enter Prime's current letters:").upper()

# Validate traits
if utils.check(traits) == True:
    print("[Error] - Traits provided are invalid: " + traits)
    sys.exit()

maxTurns = utils.default_turns
# It is possible the user provides a non-numeric argument
try:
    maxTurns = int(input("Enter Max number of transformations:"))
except:
    maxTurns = utils.default_turns
    print("[Warning] - Failed to convert to an int. Using default of " + str(maxTurns))
        
# Run word calculation
results = calculateWords(traits, words, maxTurns)



# Sort results by number turns. Lowest is shown first. 
sortedResults = sorted(results.items(), key=lambda x: x[1], reverse=False)

results_string = str()
turns = int()
score = int()
for pair in sortedResults:
    turns = pair[1][0]
    score = pair[1][1]
    if turns <= maxTurns:
        if (pair[0].lower() in wordsmith_words):
            results_string += str("{0} = {1} {2}\n".format(pair[0],turns,score))
        else:
            results_string += str("!{0} = {1} {2}\n".format(pair[0],turns,score))

print("\n---Morph's Auto Octo Finder---\n")
print("Warning, words starting with ! will not give the Wordsmith badge automatically. You will have to request for the word to be added in the #words channel\n")
print("Results are given with NewWord = NumberOfTurn NewWordScore\n---------")
print("Words within {0} turns:\n".format(maxTurns) + results_string)
