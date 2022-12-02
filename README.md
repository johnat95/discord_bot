# Pybot

This is a discord bot built with discord.py. To offer new cogs, or changes to the bot.py file, please initiate a pull request!

Requirments:
python
discord.py
python-dotenv

Installation for Python 3:

  Create virtual enviroment:

    python -m venv venv

  Activate virual enviroment:

    -Windows-

    In cmd.exe
    venv\Scripts\activate.bat

    In PowerShell
    venv\Scripts\Activate.ps1

    -Linux and Mac-
    source myvenv/bin/activate

After activating enviroment, command line should show (venv) at the start of the line.

Enter:

    pip install discord.py python-dotenv

For development testing:

Add an app through the discord development portal:

https://discord.com/login?redirect_to=%2Fdevelopers

To Run:

  While the enviroment is activated, type python bot.py to start and ctrl + c to stop
  
To update from original repo:

Add a new remote upstream repository:
 
    git remote add upstream https://github.com/aswccProgrammingClub/Pybot.git

Sync your fork:
   
    git fetch upstream
    git checkout main
    git merge upstream/main

