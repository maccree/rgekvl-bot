import discord
from discord import utils
import config

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    async def on_raw_reaction_add(self, payload):
        if payload.message_id == config.POST_ID:
            channel = self.get_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)
            member = utils.get(message.guild.members, id=payload.user_id)
