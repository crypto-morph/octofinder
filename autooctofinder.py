################################
# Octofinder - by crypto-morph #
################################

# ignore all words with this number of 'turns' or higher 
threshold = 17

# some handy subroutines

def split(word):
  return [char for char in word]

def check(word):
  return (len(start) != 8) or (start == "") or (not start.isalpha())

def findDifference(start,target):
   result = abs(start-target)
   return (result)

# Read in the words file

with open('words.txt') as f:
  words = f.read().splitlines()

# Take the name of the Prime from the command line 
results = {}
start = input("Enter Prime's current letters (or blank to exit):").lower()
if check(start):
  print("Word should be alpha and 8 characters")
else:
  print("Starting letters are: " + "|".join(split(start)))
  startValues= [0] * len(start)
  for i in range(len(start)):
     startValues[i] = ord(start[i]) - 97
  print("Starting values are: " + "|".join(str(int) for int in startValues) + "| sum = " + str(sum(startValues)))
  print("Threshold = " + str(threshold))

  # Calcuations - take the difference between the ascii values to show number of 'turns'

  for target in words:
    targetValues= [0] * len(target)
    totalmoves = 0
    for i in range(len(target)):
      targetValues[i] = ord(target[i]) - 97 
      moves = findDifference(targetValues[i],startValues[i])
      totalmoves = totalmoves + moves
    results[target] = totalmoves

# Output the result

print("results\n-----\n")
sortedresults = sorted(results.items(), key=lambda x: x[1], reverse=True)
for i in sortedresults:
  if (i[1] <= threshold):
    print(i[0] + " = " + str(i[1]))