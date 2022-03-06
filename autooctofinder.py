################################
# Octofinder - by crypto-morph #
################################

import sys, yaml

## Module with Auto Octo Finder Utilities ##

# some handy subroutines
import utils

#Init
words_file_path = str()
words = set()

# Load config YAML for discord bot key and file with words list
stream = open('bot_config.yml','r')
config = yaml.safe_load(stream)

words_file_path = config['words_file_path']

        

with open(words_file_path) as f:
    words = set(f.read().splitlines())


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
results = utils.calculateWords(traits, words, maxTurns)



# Sort results by number turns. Lowest is shown first. 
sortedResults = sorted(results.items(), key=lambda x: x[1], reverse=False)

results_string = str()
turns = int()
score = int()
for pair in sortedResults:
    turns = pair[1][0]
    score = pair[1][1]
    if turns <= maxTurns:
        results_string += str("{0} = {1} {2}\n".format(pair[0],turns,score))
        

print("\n---Morph's Auto Octo Finder---\n")
print("Results are given with NewWord = NumberOfTurn NewWordScore\n---------")
print("Words within {0} turns:\n".format(maxTurns) + results_string)
