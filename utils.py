## Constants ##
default_turns = 17
max_embed_turns = 22

gen1_traits_len = 8

# Discord's embed max size is 1024. We keep it at 800 to have a buffer
embed_max_len = 800 

dash_separator = '--------'
## Constants ##

## Helpers ##
def split(word):
  return [char for char in word]

def check(word):
  return (len(word) != gen1_traits_len) or (word == "") or (not word.isalpha())

def findDifference(start,target):
   result = abs(start-target)
   return (result)

def calculateWords(start, words, maxTurns):
   results = dict()
   for target in words:
    target = target.upper()
    totalmoves = 0
    for i in range(gen1_traits_len):
      lValue = ord(target[i])
      rValue = ord(start[i])
      moves = findDifference(lValue,rValue)
      totalmoves += moves
    if totalmoves <= maxTurns:
        results[target] = int(totalmoves)
   return results
## Helpers ##



