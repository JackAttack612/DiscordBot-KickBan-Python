# DiscordBot-KickBan-Python

# Discord Bot Application Setup
- Go to https://discord.com/developers/applications
- In the top right click the blue 'New Application' Button
- Create a Name for your Application
- Click 'Create'
- Go to the Bot Page on the left side
- Click the blue 'add a bot' button and 'yes do it'
- Enable PRESENCE INTENT, SERVER MEMBERS INTENT, and MESSAGE CONTENT INTENT
- You have now setup your bot! Continue to the next steps to configure and add the bot to your server.
 
# Basic Setup/Config
- Download the latest release https://github.com/JackAttack612/DiscordBot-KickBan-Python/releases
- Unzip the file in the directory you want
- Open the BotConfig.py file
- Change 'BOT_PREFIX_HERE' to the prefix you want for the bot
- Change the '
- How to get the bot token: Head to the application you made at https://discord.com/developers/applications. Go into your application. Click bot on the left side. Under TOKEN click the blue 'copy' button

# Instalations (Needed for bot to run properly)
- Install Python: https://www.python.org/downloads/
- Install PIP: https://pip.pypa.io/en/stable/installation/

# Imports on windows (Needed for bot to run properly)
- Go into your command terminal/prompt
- type the following: 'pip install nextcord'

# Imports on Mac OS (Needed for bot to run properly)
- Go into your command terminal/prompt
- type the following: 'python -m pip install nextcord'

# Running the bot
- Run the main.py file with python
- You will have to leave the Command Console Running in order for the bot to stay online

# Inviting the bot to your server
- Go back into your discord application at https://discord.com/developers/applications
- Click the 'OAuth2' button the the left side
- In the drop down menu below OAuth2 click on 'URL Generator'
- In the scope box select 'bot'
- In the bot permissions box select Kick Member and Ban Member or Administrator
- If you do not give the bot the right permissions it will not be able to kick or ban people!!!
- At the bottom of the page click 'copy' and paste the link into your web browser


# Commands
- Prefix goes before the commands listed
- Kick (@user) (reason)
- Ban (@user) (reason)
- Logchannel (channel or channel id)