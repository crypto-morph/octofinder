# Auto Octofinder -- Discord Bot

## What is it?

A Discord Client that serves as an interface for Auto Octo Finder. Listens to messages in the server and responds to the channel it is part of.

## Configure

Update the YAML file (bot_config.yml) with the Discord Bot Token and the file path to the words list. 

The Discord Bot Token is available after you create an application and a bot. See https://discordpy.readthedocs.io/en/stable/discord.html for instructions on how to setup a Discord bot.

## Run

1. Follow the instructions in Configure to learn how to create an application, create a bot, setting up the permissions of the bot and inviting a bot to your server.
    * Make sure that "Send Messages", "Attach Files" and "Read Messages\View Channels" are all checked.
    * For testing, you can invite the bot to a test server that you own and run the commands there.

2. To run the bot in your machine, you'll need to install the dependencies required for the script. Open a command prompt and run the following:

`pip install -r .\bot_requirements.txt`

3. Run from a python machine with `python3 discord_bot_main.py`. Take into consideration that the machine running the script owns the bot instance, so will need to be continously running for the bot to be active. 

If this is not ideal, consider using a VPS or a Cloud Instance to run the bot.

4. At this point, your Discord bot should be logged into the server you invited it to during the Configure section. Now any user can just input the command and get output from Auto Octo Finder. Command looks like this:

`!find traits maxTurns`

Example:

`!find BILLIION 15`

5. The bot will send an embed message with the list, along with a CSV for easier parsing.

## About

Thanks to Morph for sharing their Auto Octo Finder! I, Negan, just made a Discord Bot to interface with it. Thanks to Declan for sharing Octorand with us.

