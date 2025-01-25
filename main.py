import discord
from discord.ext import commands
from discord import app_commands
import os
from commands.set_gw2_api_key import set_gw2_api_key
from commands.set_gw2_guild_id import set_gw2_guild_id

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

@client.tree.command(name="set-api-key", description="Set in the bot the API key. It has to be the API key of the guild leader", guild=GUILD_ID)
async def set_api_key(interaction: discord.Integration, api_key: str):
    try:
        set_gw2_api_key(api_key)
        await interaction.response.send_message("API key set!")
    except Exception as e:
        print(f"Error setting API key: {e}")
        await interaction.response.send_message(f"Error setting API key")

@client.tree.command(name="set-guild-id", description="Set in the gw2 guild id.", guild=GUILD_ID)
async def set_guild_id(interaction: discord.Integration, guild_id: str):
    try:
        set_gw2_guild_id(guild_id)
        await interaction.response.send_message("Guild ID set!")
    except Exception as e:
        print(f"Error setting Guild Id: {e}")
        await interaction.response.send_message(f"Error setting Guild ID")

client.run(os.environ["DISCORD_TOKEN"])