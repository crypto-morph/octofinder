# Auto Octofinder

## The Quest

Would you like to know the 'easiest' words that your (Octorand Prime)[https://octorand.com/] can be renamed to from a big dictionary of 8 letter words? If so, read on! 

## What is it?

This script takes the current 'name' of an (Octorand Prime)[https://octorand.com/] from the command line and calculates the number of 'turns' it would take to make all the words defined in `words.txt`.

## Configure

Edit line 6 of the script to set the threshold (default: 17).  No word with more than this number of turns will be printed. 

## Run

Run from a python machine with `python3 autocryptofinder.py` - or use https://trinket.io/features/python3 from the Web (you'll have to import both `words.txt` and `autooctofinder.py`)

## Adding more words

The words are stored in `words.txt` and are newline seperated - just add extra words on the end or remove rubbish words as you go!

## Example run

```
Enter Prime's current letters (or blank to exit):algorand
Starting letters are: a|l|g|o|r|a|n|d
Starting values are: 0|11|6|14|17|0|13|3| sum = 64
Threshold = 17
results
-----
agiotage = 17
alginate = 17
allopath = 17
bedstand = 17
blipping = 17
comorbid = 17
honorand = 17
ephorate = 16
aldolase = 15
blinkard = 15
endosarc = 15
biennale = 14
biforate = 12
```

(Note: blipping is an awesome word)