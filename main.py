import discord
from discord import utils
import config

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    async def on_raw_reaction_add(self, payload):
