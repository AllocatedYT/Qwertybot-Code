import os

# The prefix that will be used to parse commands.
# It doesn't have to be a single character!
COMMAND_PREFIX = "q!"

# The bot token. Keep this secret!
BOT_TOKEN = "NzU2OTc3NDIzNzU2ODIwNTcy.X2ZsKQ.HgZ943kJhe4Otjz64kJ3i5biY3w"

# The now playing game. Set this to anything false-y ("", None) to disable it
NOW_PLAYING = COMMAND_PREFIX + "commands"

# Base directory. Feel free to use it if you want.
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
