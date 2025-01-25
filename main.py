import discord
from discord.ext import commands
from discord import app_commands
import os

GUILD_ID = discord.Object(id=os.environ["DISCORD_SERVER_ID"])

class Client(commands.Bot):
    async def on_ready(self):
        print(f"Logged in as {self.user}")        
        try:
            guild = discord.Object(id=os.environ["DISCORD_SERVER_ID"])
            synced = await self.tree.sync(guild=guild)
            print(f"Synced {len(synced)} commands to guild {guild.id}")
        except Exception as e:
            print(f"Error syncing commands: {e}")

    async def on_message(self, message):
        if message.author == self.user:
            return

intents  = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)

@client.tree.command(name="hello", description="Say hello", guild=GUILD_ID)
async def hello(interaction: discord.Integration):
    await interaction.response.send_message("Hello there!")

client.run(os.environ["DISCORD_TOKEN"])