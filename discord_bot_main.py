## Discord API ##
import discord
from discord import channel
from discord.ext import tasks
## Discord API ##

## Module with Auto Octo Finder Utilities ##
import utils

## YAML used for configuring data fields ##
import yaml

## Simple class that derives from discord.Client. Implement
## event handlers to customize behavior.
class DiscordClientBot(discord.Client):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)

        self.words_file_path = str()
        self.words = set()

    def loadWords(self):
        with open(self.words_file_path) as f:
            self.words = set(f.read().splitlines())

    async def runAutoOctoFinder(self, message):
        
        # We'll use the source channel as the destination of the messages.
        channel = message.channel

        # Validation on how many arguments to expect.
        expected_num_args = 3
        
        # Assume the format of the message is: "!find traits turnsMax"
        split_msg = str(message.content).split(" ")
        print("[Info] - Processing command: " + str(split_msg))
        
        num_args = len(split_msg)
        if  num_args != expected_num_args:
            print("[Error] - Command has an invalid number of arguments."
            "{0} provided, but {1} expected".format(num_args, expected_num_args))
            await message.channel.send(
                "Beep Boop! The command should be in the following format: \n"
                "!find traits turns")
            return

        traits = str()
        traits = split_msg[1].upper()

        # Validate traits
        if utils.check(traits) == True:
            print("[Error] - Traits provided are invalid: " + traits)
            await message.channel.send(
                "Beep Boop! Traits must have only 8 letters")
            return
        
        maxTurns = utils.default_turns
        # It is possible the user provided a non-numeric argument
        try:
            maxTurns = int(split_msg[2])
        except:
            maxTurns = utils.default_turns
            print("[Warning] - Failed to convert second parameter to an int. Using default of " + str(maxTurns))
            await message.channel.send(
                "Beep Boop! Turns argument couldn't be read. Using default: " + str(maxTurns))
        
        # Run word calculation
        results = utils.calculateWords(traits, client.words, maxTurns)

        # Sort results by number turns. Lowest is shown first. 
        sortedResults = sorted(results.items(), key=lambda x: x[1], reverse=False)
        print("Results from word calculation: " + str(results))

        # Build a message with the results #

        # Header embed is separate from the results embed to work around max lenght
        # limitation.
        header_embed = discord.Embed()
        header_embed.add_field(name=
        "---Morph's Auto Octo Finder---\n\nWords within {0} turns:\n".format(maxTurns), value="---------",inline=True)
        await channel.send(embed=header_embed)
        
        embed_results_string = str()
        turns = int()
        for pair in sortedResults:
            turns = pair[1]
            if turns <= maxTurns:
                embed_results_string += str("{0} = {1}\n".format(pair[0],pair[1]))

                if len(embed_results_string) >= utils.embed_max_len:
                    sub_embed = discord.Embed()
                    sub_embed.add_field(name=utils.dash_separator,value=embed_results_string,inline=False)
                    await channel.send(embed=sub_embed)
                    embed_results_string = ''
                    if(maxTurns >= utils.max_embed_turns):
                        break
        
        if len(embed_results_string):
            sub_embed = discord.Embed()
            sub_embed.add_field(name=utils.dash_separator,value=embed_results_string,inline=False)
            await channel.send(embed=sub_embed)

        ## Also provide a CSV for easier inspection ##
        results_file_name = "{0}_{1}_words.csv".format(traits, maxTurns)
        f = open(results_file_name,"w",encoding="utf-8")

        csv_content = "WORDS,TURNS"
        for item in sortedResults:
            csv_content += ("{0},{1}\n".format(item[0],item[1]))
        
        f.write(csv_content)
        f.close()

        await channel.send(file=discord.File(f.name))

if __name__ == '__main__':

    # Create our Discord bot.
    client = DiscordClientBot()
    
    # Implement event handlers
    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))
        client.loadWords()

    # Event handler whenever a message is received in the channel the bot is listening.
    @client.event
    async def on_message(msg):

        if msg.content.startswith('!find'):
            await client.runAutoOctoFinder(msg)

    # Load config YAML for discord bot key and file with words list
    stream = open('bot_config.yml','r')
    config = yaml.safe_load(stream)

    client.words_file_path = config['words_file_path']
    client.run(config['bot_key'])
