# Auto Octofinder -- Discord Bot

## What is it?

A Discord Client that serves as an interface for Auto Octo Finder. Listens to messages in the server and responds to the channel it is part of.

## Configure

Update the YAML file (bot_config.yml) with the Discord Bot Token and the file path to the words list. 

See https://discordpy.readthedocs.io/en/stable/discord.html for instructions on how to setup a Discord bot.

## Run

1. Install the dependencies required for the script to run by opening a command prompt and running the following:

`pip install -r .\bot_requirements.txt`

2. Run from a python machine with `python3 discord_bot_main.py`. Take into consideration that the machine running the script will act as a 'host', so will need to be continously running for the bot to be active. 

If this is not ideal, consider using a VPS or a Cloud Instance to run the bot.

3. At this point OctoBot should be logged in in the server you invited it to during the Configure section. Now any user can just input the command and get the output from Auto Octo Finder. Command looks like this:

`!find traits maxTurns`

Example:

`!find BILLIION 15`

4. The bot will send an embed message with the list, along with a CSV for easier parsing.

## About

Thanks to Morph for sharing their Auto Octo Finder! I, Negan, just made a Discord Bot to interface with it. Thanks to Declan for sharing Octorand with us.