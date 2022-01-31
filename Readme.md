# Auto Octofinder

## The Quest

This tool helps with the [Octorand](https://octorand.com/) game. In Octorand there are 1000 Prime Octorand NFTs in existance and they all have randomly generated names - 8 letters long.   They generate a crypto-token called an [Octo](https://tinychart.org/asset/559219992) on a fixed schedule.  They sit on the Algorand blockchain.   

You can rename your Octorand - but the rules are:
  * you can only move one letter at a time
  * they can only move one step in the alphabet (a "C" can only become a "B" or a "D")
  * Each move costs 10 of your hard earned Octo   

Thus it becomes interesting to the average Octorand Prime owner to know which words are 'easiest' from your starting position. 

## What is it?

This Python script takes the current 'name' of an [Octorand Prime](https://octorand.com/) from the command line and calculates the number of 'turns' it would take to make all the words defined in `words.txt`.

## Configure

Edit line 6 of the script to set the threshold (default: 17).  No word with more than this number of 'turns' will be printed.

If you set this higher, the list gets very long very quickly. 

## Run

Run from a python machine with `python3 autocryptofinder.py` - or use [Trinket](https://trinket.io/features/python3) from the Web (you'll have to import both `words.txt` and `autooctofinder.py`)

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

Hope this helps someone - I am no Python Programmer - but enjoyed learning how to do this in Python - and help support an amazing Algorand based project!