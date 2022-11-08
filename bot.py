import discord
from discord.ext.commands import Bot
from discord.ext.commands.core import has_permissions
from discord.utils import async_all

intents = discord.Intents.all()
intents.members = True
intents.guilds = True
client = Bot(command_prefix = '!', intents=intents, help_command=None)

@client.command(pass_context = True)
async def grep(ctx):
    count = 0
    x = ctx.channel
    async for message in x.history(limit=5000):
        if len(message.attachments) > 0:
            for attachment in message.attachments:
                await attachment.save(str(count) + '.png')
                count = count + 1

client.run('TOKEN')
